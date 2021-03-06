
from datetime import date
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404, render
from . models import Post
from .forms import Comment_form
from django.views import View
# Create your views here.

#======================================================================
class StartingPageview(ListView):
    template_name="blog/index.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"              # by default object name is listobject so we have to rename it
    
    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data   
    
#-----------------------OR we can use function---------------------------------------
'''def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{"posts":latest_posts})
'''
#=======================================================================

#=========================================================================
class Postview(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"

#------------------------OR---------------------------------------------
'''
def post(request):
    arrange_posts=Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{"all_posts":arrange_posts})
'''
#========================================================================


#======================================================================
class Postdetailview(View):

    def is_save_later(self,request,post_id):
        stored_posts=request.session.get("stored_posts")
        if stored_posts is not None:
            save_later= post_id in stored_posts
        else:
            save_later= False
        return save_later        

    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        context={
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":Comment_form(),
           "show_comments":post.comments.all().order_by("-id"),
           "savelater":self.is_save_later(request,post.id)
        }
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slug):
        comment=Comment_form(request.POST)
        post=Post.objects.get(slug=slug)
        if comment.is_valid():
            comm=comment.save(commit=False)
            comm.post=post
            comm.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))

        context={
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":Comment_form(),
            "show_comments":post.comments.all().order_by("-id"),
            "savelater":self.is_save_later(request,post.id)
        }
        return render(request,"blog/post-detail.html",context)
    

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] =self.object.tag.all() 
        context['comment_form']=Comment_form()
        return context
    '''
#--------------------------OR-------------------------------------------    
'''
def post_detail(request,slug):
    inventory=get_object_or_404(Post,slug=slug)
    return render(request,"blog/post-detail.html",{"post":inventory,"post_tags":inventory.tag.all()})
'''
#====================================================================================================    


class savelater(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}

        if stored_posts is None or len(stored_posts) ==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            context["posts"]=posts
            context["has_posts"]=True

        return render(request,"blog/stored-posts.html",context)    



    def post(self,request):
        stored_posts=request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts=[]

        post_id=int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)    

        request.session["stored_posts"]=stored_posts

        return HttpResponseRedirect("/")    