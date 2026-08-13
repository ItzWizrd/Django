from rest_framework import serializers

from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "description",
            "price",
            "quantity",
            "manufacture_date",
            "expiry_date",
        ]
        read_only_fields = ["manufacture_date", "expiry_date"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
