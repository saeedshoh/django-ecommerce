from operator import call

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


def category_product_list_view(request, cit):
    # dd(cit)
    category = Category.objects.get(cit=cit)
    products = Product.objects.filter(product_status='published', category=category)

    return render(request, 'core/categories/product-list.html', {
        'category': category,
        'products': products
    })
