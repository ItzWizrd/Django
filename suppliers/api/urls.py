from django.urls import path, re_path

from .views import SupplierDetailAPIView, SupplierListAPIView


urlpatterns = [
    re_path(r"^create/?$", SupplierListAPIView.as_view(), name="supplier-list"),
    path(
        "edit-delete-get-supplier/<int:pk>/",
        SupplierDetailAPIView.as_view(),
        name="supplier-detail",
    ),
]
