from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Category, Product

class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, id=category_id)
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context