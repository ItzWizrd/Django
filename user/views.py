from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import Userform

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    paginate_by = 10
    queryset = User.objects.select_related("role").order_by("-pk")

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = Userform
    success_url = reverse_lazy("user:user-list")

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = Userform
    success_url = reverse_lazy("user:user-list")
    
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("user:user-list")


