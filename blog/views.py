from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def home_view(request, *args, **kwargs):
    posts = Post.objects.filter(status="PUBLISHED")
    context_data = {
        "title": "Home Page | Posts",
        "posts": posts,
    }
    return render(request, "blog/index.html", context_data)



