from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.OrderAdd.as_view(), name='order_create'),
    path('orders/update/<int:pk>/', views.OrderUpdate.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
]