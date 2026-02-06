from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def products_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()  # добавляем категории для фильтров
    return render(request, 'products.html', {'products': products, 'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})
