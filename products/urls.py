from django.urls import path
from .views import ProductListView, ProductDetailView, ToggleFavoriteView, TimeReportView, CategoryListView, \
    SubCategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/favorite/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('projects/time-report/', TimeReportView.as_view(), name='project-time-report'),
    path('products/categories/', CategoryListView.as_view(), name='category-list'),
    path('products/subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),

]
