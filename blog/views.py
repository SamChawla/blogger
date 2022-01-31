from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
# Create your views here.


def home_view(request, *args, **kwargs):
    posts = Post.objects.filter(status="PUBLISHED")
    context_data = {
        "title": "Home Page | Posts",
        "posts": posts,
    }
    return render(request, "blog/index.html", context_data)


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status="PUBLISHED")
    context_object_name = "posts"
    ordering = ["-modified_at"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["title"] = "Home Page | Posts"
        return data

post_list_view = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["title"] = ""
        return data

post_detail_view = PostDetailView.as_view()



