from django.db import models
from django.utils.timezone import localdate
from customer.models import Customer

# Create your models here.
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "Pending"
        PROCESSING = "Processing"
        SHIPPED = "shipped"
        DELIVERED = "delivered"
        CANCELLED = "cancelled"
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=localdate, blank=True)
    status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    order_details = models.ManyToManyField("product.Product")

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
