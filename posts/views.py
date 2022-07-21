import re
from django.shortcuts import render

import posts
from .models import Post
# Create your views here.

# index function


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


# def post(request, pk):
#     posts = Post.objects.get(id=pk)
#     return render(request, 'post.html', {'posts': posts})


def blog(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'blog.html', {'posts': posts})

def webdesign(request):
    return render(request, 'webdesign.html')