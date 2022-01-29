from django.contrib import admin
from django.urls import path
from accounts import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
]
