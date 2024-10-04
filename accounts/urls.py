# account/urls.py
from django.urls import path
from .views import register, login_view, logout_view, profile, user_list

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('users/', user_list, name='user_list'),  # This is correct
]
