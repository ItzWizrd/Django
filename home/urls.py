from django.urls import path
from .views import index_view, login_view, Signup_view, dashboard_view, logout_view

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', Signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
 ]