from django.shortcuts import render
from .models import post
# Create your views here.


def home(request):
    posts = post.objects.all()
    return render(request, 'index.html', {'posts' : posts})

def posts(request, post_id):
    post_by_id = post.objects.get(id=int(post_id))
    return render(request, 'post.html', {'posts': post_by_id})