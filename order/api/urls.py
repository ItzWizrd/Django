from django.urls import path, re_path

from order.api.views import OrderDetailAPIView, OrderListAPIView

urlpatterns = [
    re_path(r'^create/?$', OrderListAPIView.as_view(), name='order-list'),
    path('edit-delete-get-order/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail')
]
