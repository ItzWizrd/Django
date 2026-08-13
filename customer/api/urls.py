from django.urls import path, re_path

from .views import CustomerDetailAPIView, CustomerListAPIView


urlpatterns = [
    re_path(r"^create/?$", CustomerListAPIView.as_view(), name="customer-list"),
    path(
        "edit-delete-get-customer/<int:pk>/",
        CustomerDetailAPIView.as_view(),
        name="customer-detail",
    ),
]
