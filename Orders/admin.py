from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('order_id', 'customer__name', 'status')
    filter_horizontal = ('order_details',)
    readonly_fields = ('order_date',)
