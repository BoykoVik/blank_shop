from django.shortcuts import render, get_list_or_404
from .models import Category, Product

#список товаров и вывод по категориям
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_list_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'myshop/product/list.html',
    {'category': category,
    'categories': categories,
    'products': products})

#страница каждого товара
def product_detail(request, id, slug):
    product = get_list_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'myshop/product/detail.html', {'product': product})
