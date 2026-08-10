from .models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from .forms import Userform


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = Userform
    template_name = 'users/add_users.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = Userform
    template_name = 'users/update_users.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        if form.cleaned_data.get('password'):
            form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_users.html'
    success_url = reverse_lazy('user-list')
