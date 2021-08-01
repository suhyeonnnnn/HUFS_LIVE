from django.shortcuts import get_object_or_404, render
from .models import Post

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk= post_id) 

    return render(request, 'detail.html', {'post':post_detail})