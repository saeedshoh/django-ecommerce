from django.http import HttpResponse
from django.shortcuts import render

from core.models import Product, Category, Vendor


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


def vendor_list(request):
    vendors = Vendor.objects.all()

    return render(request, 'core/vendors/list.html', {
        'vendors': vendors
    })


def vendor_detail(request, vid):
    vendor = Vendor.objects.prefetch_related('products').get(vid=vid)
    return render(request, 'core/vendors/detail.html', {
        'vendor': vendor
    })

def product_detail(request, pid):
    product = Product.objects.get(pid=pid)

    return render(request, 'core/products/detail.html', {
        'product': product
    })
