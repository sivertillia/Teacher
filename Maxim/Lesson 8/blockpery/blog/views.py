from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def hello(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts":posts})

def get_post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "blog/blog_detail.html", context={"post": post})