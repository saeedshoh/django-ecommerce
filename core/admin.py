from django.contrib import admin
from core.models import User, CartOrder, CartOrderItem, Wishlist, ProductReview, Product, ProductImage, Tag, Address, \
    Category, Vendor


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['title', 'category', 'user', 'product_image', 'price', 'featured', 'product_status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']


@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'created_at', 'product_status']


@admin.register(CartOrderItem)
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_number', 'item', 'image', 'quantity', 'price', 'total']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']
