from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone', 'address')
    readonly_fields = ('created_at', 'updated_at')
    