from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')