from django.contrib import admin

from web_shop_0_1.products.models import Products, ProductClass, ProductType


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = ['product_class', 'brand', 'product_type', 'supplier']
    search_fields = ['name']
    list_per_page = 10


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ['class_name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
