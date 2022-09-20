from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_index(request):
    blogs=Blog.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request,'blog_index.html',context)
def blog_detail(request):
    blog=Blog.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)