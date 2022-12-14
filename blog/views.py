from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts
        }
    )

def postDetail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/postdetail.html',
        {
            'post' : post
        }
    )
