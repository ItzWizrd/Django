from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from order.models import Order

from .forms import UserSignUpForm


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("admin:login")
    else:
        form = UserSignUpForm()
    return render(request, "home/signup.html", {"form": form})


def login_view(request): 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:dashboard")
        else:      messages.error(request, "Invalid username or password.")
    else:

        return render(request, "home/login.html")        


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("admin:login")
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    orders_by_status = Order.objects.values("status").annotate(count=Count("status"))
    context = {
        "total_users": total_users,
        "total_orders": total_orders,
        "orders_by_status": orders_by_status,
    }
    return render(request, "home/dashboard.html", context)


def logout_view(request):
    logout(request)
    return redirect("admin:login")
