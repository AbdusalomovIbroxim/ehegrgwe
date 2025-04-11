from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'name', 'email',
            'first_name', 'last_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'name', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

