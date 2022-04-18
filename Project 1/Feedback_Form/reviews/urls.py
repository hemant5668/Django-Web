from django import views
from django.urls import path
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankyouView.as_view()),
    path("reviewlist", views.ReviewlistView.as_view()),
    path("reviewlist/favourite", views.addfavourite.as_view()),
    path("reviewlist/<int:pk>", views.Singlereview.as_view())
]


