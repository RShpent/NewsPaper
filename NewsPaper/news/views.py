from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Category

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news_one'



