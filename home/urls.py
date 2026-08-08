from django.urls import path
from django.views.generic import RedirectView

from .views import login_view, signup_view, dashboard_view, logout_view

app_name = "home"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="admin:index"), name="root"),
    path("signup", signup_view, name="signup-no-slash"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("logout/", logout_view, name="logout"),
]
