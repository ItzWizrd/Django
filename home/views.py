from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from order.models import Order
from product.models import Product

from .forms import LoginForm, UserSignUpForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home:dashboard")

        messages.error(request, "Invalid username or password.")

    form = LoginForm()
    return render(request, "home/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("home:login")
    else:
        form = UserSignUpForm()
    return render(request, "home/signup.html", {"form": form})


@login_required(login_url="home:login")
def dashboard_view(request):
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    total_products = Product.objects.count()

    status_count = {
        "pending": Order.objects.filter(status=Order.OrderStatus.PENDING).count(),
        "processing": Order.objects.filter(status=Order.OrderStatus.PROCESSING).count(),
        "shipped": Order.objects.filter(status=Order.OrderStatus.SHIPPED).count(),
        "delivered": Order.objects.filter(status=Order.OrderStatus.DELIVERED).count(),
        "cancelled": Order.objects.filter(status=Order.OrderStatus.CANCELLED).count(),
    }

    context = {
        "total_orders": total_orders,
        "total_users": total_users,
        "total_products": total_products,
        "status_count": status_count,
    }
    return render(request, "home/dashboard.html", context)


def logout_view(request):
    logout(request)
    return redirect("home:login")
