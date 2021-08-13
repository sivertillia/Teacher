from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .forms import TagForm
# Create your views here.
def hello(request):
    post = Post.objects.all()
    return render(request, "blog/index.html", context={'posts': post})

class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/blog_detail.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context= {'tags': tags})

class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_post.html', context={'tag': tag})

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        # print(request.POST)
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            print(new_tag)
            return redirect()
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

