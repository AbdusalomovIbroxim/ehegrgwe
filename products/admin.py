from django.contrib import admin
from .models import Category, SubCategory, Product, Project


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'category', 'price', 'discount', 'discounted_price', 'rating', 'review_count', 'favorites_count')
    list_filter = ('category', 'subcategory', 'favorites')
    search_fields = ('name', 'category__name', 'subcategory__name')

    def favorites_count(self, obj):
        return obj.favorites.count()

    favorites_count.admin_order_field = 'favorites'
    favorites_count.short_description = 'Favorites Count'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'duration', 'time_remaining')
    search_fields = ('name',)

    def time_remaining(self, obj):
        remaining_time = obj.get_time_remaining()
        return f"{remaining_time['days']}d {remaining_time['hours']}h {remaining_time['minutes']}m {remaining_time['seconds']}s"

    time_remaining.admin_order_field = 'time_remaining'
    time_remaining.short_description = 'Time Remaining'


# Регистрируем модели в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Project, ProjectAdmin)
