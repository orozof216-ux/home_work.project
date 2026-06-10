from django.urls import path
from .views import register, login_user, confirm_user

urlpatterns = [
    path('register/', register),
    path('login/', login_user),
    path('confirm/', confirm_user),
]