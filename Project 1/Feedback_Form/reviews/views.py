
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Reviewforms1
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView



# Create your views here.

class ReviewView(View):                   
    
    '''there is a formview which can handle all get and post , there is create view option also
    which deals which form it generate a form accordingly to model and save you only have to point model'''                                         


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


#----------------------------------------------------------------------------------------------------------------------------------

class ThankyouView(TemplateView):
    template_name="reviews/thankyou.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] ="Today is our day!" 
        return context
    


def thank_you(request):
    return render(request,"reviews/thankyou.html")    


#----------------------------------------------------------------------------------------------------------------------------------
'''class ReviewlistView(TemplateView):
    template_name="reviews/reviewlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_list=Review.objects.all()        
        context["review"] = review_list
        return context
'''


 # or you can use ListView   
class ReviewlistView(ListView):
    template_name="reviews/reviewlist.html"
    model=Review
    context_object_name="review"

    ''' def get_queryset(self):                               #for filter data
        base=super().get_queryset()
        data=base.filter(rating__gt=3)
        return data
    '''





#----------------------------------------------------------------------------------------------------------------------------------
'''class Singlereview(TemplateView):
    template_name="reviews/singlereview.html"

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        review_id=kwargs['id']
        singelview=Review.objects.get(pk=review_id)
        context["singelreview"] =singelview
        return context
'''    

# or youcan use dertail view    
class Singlereview(DetailView):
    template_name="reviews/singlereview.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        fav_id=request.session.get("fav")
        context["userfav"] = fav_id==str(loaded_review.id)
        return context

class addfavourite(View):
    def post(self, request):
        review_id=request.POST["review_id"]
        request.session["fav"]=review_id
        return HttpResponseRedirect("/reviewlist/"+review_id)

    

