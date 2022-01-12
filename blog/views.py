from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    # html="<h1> Hello World </h1>"
    # return HttpResponse(html)
    return render(request, "base.html", {"title": "HOME PAGE"})



