from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .forms import PostForm, TagForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def blog(request):
    post = Post.objects.all()
    return render(request, "blog/index.html", context={'posts': post})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/blog_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_post.html', context={'tag': tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag.get_absoluter_url())
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag.get_absoluter_url())
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


class TagDelete(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_delete.html', context={'tag': tag})

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        tag.delete()
        return redirect('/blog/tags')


class PostDelete(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_delete.html', context={'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        post.delete()
        return redirect('/blog')

    login_url = '/'
    redirect_field_name = 'blog_url'

class PostUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', context={'form': form, 'post': post})
    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post.get_absoluter_url())
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

    login_url = '/'
    redirect_field_name = 'blog_url'

def log_out(request):
    logout(request)
    return redirect('blog_url')