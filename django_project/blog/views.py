from django.shortcuts import render
from .models import Post

def home(req):
    context = {
        "posts": Post.objects.all(),
        "title": "Django-Home"
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {"title": "Django-About"})
