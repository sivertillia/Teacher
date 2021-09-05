from django.shortcuts import redirect


def redirectBlog(request):
    return redirect('blog_url')