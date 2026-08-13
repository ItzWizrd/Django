from django.urls import path, re_path

from .views import (
    CategoryDetailAPIView,
    CategoryListAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
)


urlpatterns = [
    re_path(r"^create/?$", ProductListAPIView.as_view(), name="product-list"),
    path(
        "edit-delete-get-product/<int:pk>/",
        ProductDetailAPIView.as_view(),
        name="product-detail",
    ),
    re_path(r"^categories/create/?$", CategoryListAPIView.as_view(), name="category-list"),
    path(
        "categories/edit-delete-get-category/<int:pk>/",
        CategoryDetailAPIView.as_view(),
        name="category-detail",
    ),
]
