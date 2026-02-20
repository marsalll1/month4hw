from django.urls import path
from .views import CategoryListView, ProductListView, CategoryProductsView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
]