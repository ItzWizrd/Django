from django.urls import reverse_lazy
from .models import Product, Category
from django.views.generic import UpdateView,DeleteView,CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm, CategoryForm

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = "product/category_list.html"
    context_object_name = 'category_list'


class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "product/category_create.html"
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "product/category_update.html"
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = "product/category_delete.html"
    success_url = reverse_lazy('category-list')

class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = 'product_list'

class ProductCreateView(LoginRequiredMixin,CreateView):
     model = Product
     form_class = ProductForm
     template_name = "product/product_create.html"
     success_url = reverse_lazy('product-list')

class ProductUpdateView(LoginRequiredMixin,UpdateView):
     model = Product
     form_class = ProductForm
     template_name = "product/product_update.html"
     success_url = reverse_lazy('product-list')


class ProductDeleteView(LoginRequiredMixin,DeleteView):
     model = Product
     template_name = "product/product_delete.html"
     success_url = reverse_lazy('product-list')
