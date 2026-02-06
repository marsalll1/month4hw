from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list),
    path('products/', views.products_list),
    path('category/<int:category_id>/', views.category_products),
]
