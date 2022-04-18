
from datetime import date
from urllib import request
from django.shortcuts import get_object_or_404, render
from . models import Post
# Create your views here.

def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{"posts":latest_posts})

def post(request):
    arrange_posts=Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{"all_posts":arrange_posts})

def post_detail(request,slug):
    inventory=get_object_or_404(Post,slug=slug)
    return render(request,"blog/post-detail.html",{"post":inventory,"post_tags":inventory.tag.all()})