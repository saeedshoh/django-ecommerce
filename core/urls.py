"""
URL configuration for ecomprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
<<<<<<< HEAD
from .views import index, product_list, categories_list, category_product_list_view
=======
from .views import index, product_list, categories_list, vendor_list, vendor_detail, product_detail
>>>>>>> 2773a05643a3a2e49115d06836d7b5d11bd306ca
from django.conf.urls.static import static
from django.conf import settings
app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('products/', product_list, name="product_list"),
    path('products/<pid>/', product_detail, name="product_detail"),

    path('categories/', categories_list, name="categories_list"),
<<<<<<< HEAD
    path('categories/<str:cit>/', category_product_list_view, name="category_product_list"),
=======

    path('vendors/', vendor_list, name="vendor_list"),
    path('vendors/<vid>/', vendor_detail, name="vendor_detail"),
>>>>>>> 2773a05643a3a2e49115d06836d7b5d11bd306ca
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
