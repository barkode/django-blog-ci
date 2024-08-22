from django.shortcuts import render  # noqa
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
