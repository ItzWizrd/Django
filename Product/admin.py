from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name',  'manufacture_date', 'expiry_date', 'price', 'quantity', 'description')
    search_fields = ('product_name',)
    list_filter = ('manufacture_date', 'expiry_date')
    readonly_fields = ('manufacture_date', 'expiry_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)
