from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.name