from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create/', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
]
