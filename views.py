from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def jadval(request):
    html="""
    <h1>JADVAL<h2>
    """
    return HttpResponse(html)

def post_royxat(request):
    posts=Post.objects.all()
    post_roy=''
    for post in posts:
        post_roy+=f"<li>{post}</li>"
    return HttpResponse(f"<ul>{post_roy}</ul>")
