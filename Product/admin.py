from django.contrib import admin
from .models import Product, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')    