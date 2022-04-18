from django.urls import path
from . import views
urlpatterns = [
    path("", views.Createinputprofile.as_view()),
    path("list",views.userlist.as_view())
]