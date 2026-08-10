from django.urls import path
from django.views.generic import RedirectView

from .views import dashboard_view, login_view, logout_view, signup_view

app_name = "home"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="home:dashboard"), name="root"),
    path("login", login_view, name="login-no-slash"),
    path("login/", login_view, name="login"),
    path("signup", signup_view, name="signup-no-slash"),
    path("signup/", signup_view, name="signup"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]
