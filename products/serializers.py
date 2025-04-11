from rest_framework import serializers
from .models import Product, Category, SubCategory, Project


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'price', 'discount', 'discounted_price',
            'rating', 'review_count', 'category', 'subcategory', 'is_favorite'
        ]

    def get_is_favorite(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and obj.favorites.filter(id=user.id).exists()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'duration']
