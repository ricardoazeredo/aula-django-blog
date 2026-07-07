from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'home.html')



def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post': post})