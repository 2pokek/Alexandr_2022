from django.shortcuts import render
from .models import Post,Comment


# Create your views here.
def blog_index(request):
    posts=Post.objects.all().order_by('created_on')
    context ={
        'posts':posts
    }
    return render(request,'blog_index.html',context)
def blog_detail(request):
    post=Post.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments':comments,
    }
    return render(request, 'blog_detail.html', context)