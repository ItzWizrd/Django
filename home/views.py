# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import UserSignupForm, LoginForm
from Orders.models import Order
from product.models import Product


def index_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    form = LoginForm()
    return render(request, 'home/login.html', {'form': form})


def Signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'home/signup.html', {'form': form})


@login_required(login_url='login')
def dashboard_view(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    status_count = {
        'pending': Order.objects.filter(status=Order.OrderStatus.PENDING).count(),
        'processing': Order.objects.filter(status=Order.OrderStatus.PROCESSING).count(),
        'shipped': Order.objects.filter(status=Order.OrderStatus.SHIPPED).count(),
        'delivered': Order.objects.filter(status=Order.OrderStatus.DELIVERED).count(),
        'cancelled': Order.objects.filter(status=Order.OrderStatus.CANCELLED).count(),
    }
    context = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_products': total_products,
        'status_count': status_count,
    }
    return render(request, 'home/dashboard.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')
