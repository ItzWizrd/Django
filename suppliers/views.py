



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_create.html'
    success_url = reverse_lazy('supplier-list')


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers/supplier_update.html'
    success_url = reverse_lazy('supplier-list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_delete.html'
    success_url = reverse_lazy('supplier-list')
