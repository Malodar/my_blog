from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


class IndexView(ListView):
    model = Post
    template_name = 'blog/blog_main.html'
    categories = [i[1] for i in Post.CATEGORIES_CHOICES]
    extra_context = {
        'categories': categories,
    }
