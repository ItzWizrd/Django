from django.urls import path
from Orders.api.views import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('edit-delete-get-order/<int:pk>/',OrderDe)   
    
    ]