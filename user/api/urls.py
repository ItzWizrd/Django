from django.urls import path, re_path

from .views import RoleDetailAPIView, RoleListAPIView, UserDetailAPIView, UserListAPIView


urlpatterns = [
    re_path(r"^create/?$", UserListAPIView.as_view(), name="user-list"),
    path("edit-delete-get-user/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    re_path(r"^roles/create/?$", RoleListAPIView.as_view(), name="role-list"),
    path("roles/edit-delete-get-role/<int:pk>/", RoleDetailAPIView.as_view(), name="role-detail"),
]
