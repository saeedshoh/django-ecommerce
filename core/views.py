from django.http import HttpResponse
from django.shortcuts import render

from core.models import Product, Category


def index(request):
    products = Product.objects.filter(featured=True, product_status='published')

    return render(request, 'core/home.html', {
        'products': products
    })


def product_list(request):
    products = Product.objects.filter(product_status='published')

    return render(request, 'core/products/list.html', {
        'products': products
    })


def categories_list(request):
    categories = Category.objects.all()

    return render(request, 'core/categories/list.html', {
        'categories': categories
    })
