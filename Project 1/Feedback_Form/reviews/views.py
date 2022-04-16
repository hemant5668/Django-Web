
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Reviewforms1
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self,request):
        form=Reviewforms1()
        return render(request,"reviews/reviews.html",{"form":form})

    def post(self,request):
        form=Reviewforms1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request,"reviews/reviews.html",{"form":form})


def reviews(request):
    if request.method=="POST":
        form=Reviewforms1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form=Reviewforms1()

    return render(request,"reviews/reviews.html",{"form":form})

def thank_you(request):
    return render(request,"reviews/thankyou.html")    