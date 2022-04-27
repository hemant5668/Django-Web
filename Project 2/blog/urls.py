from django.urls import path
from . import views

urlpatterns = [
    path("posts",views.Postview.as_view(),name="post-page"),          #views.post is used to call function for all posts  
    path("",views.StartingPageview.as_view(),name="starting-page"),   #views.starting_page is used to call defined function
    path("posts/<slug:slug>",views.Postdetailview.as_view(),name="post-detail-page"),  #views.post_detail 
    path("read-later",views.savelater.as_view(),name="read-later")  #views.post_detail 
]