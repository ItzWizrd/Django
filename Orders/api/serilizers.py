from rest_framework import serializers
from Orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer", "product", "quantity", "total_price", "order_date", "status"]