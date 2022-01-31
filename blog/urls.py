from django.contrib import admin
from django.urls import path
from blog.views import (
    home_view,
    post_list_view,
    post_detail_view,
)

urlpatterns = [
    path("",home_view, name="home"),
    path("posts/", post_list_view, name="blog-home"),
    path("posts/<int:pk>/", post_detail_view, name="blog-post"),
]
