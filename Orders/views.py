from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Order
from .forms import OrdersForm
from django.core.paginator import Paginator

def order_list(request):
    orders_list = Order.objects.all()
    paginator = Paginator(orders_list,25)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    return render(request, 'orders/order_list.html', {'orders': orders})

    

class OrderAdd(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrdersForm
    template_name = "orders/orders_create.html"
    success_url = reverse_lazy('order_list')

class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrdersForm
    template_name = "orders/orders_update.html"
    success_url = reverse_lazy('order_list')

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/orders_delete.html"
    success_url = reverse_lazy('order_list')