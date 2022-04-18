
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from . forms import ProfileForm
from .models import uploads
# Create your views here.

'''def storeimg(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
'''

class Createinputprofile(View):
    def get(self,request):
        form=ProfileForm
        return render(request,"profiles/create_profile.html",{"form":form})

    def post(self,request):
        submit_form = ProfileForm(request.POST, request.FILES)
        if submit_form.is_valid():
            profile=uploads(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request,"profiles/create_profile.html",{"form":submit_form})
        

class userlist(ListView):
    template_name="profiles/userprofile.html"
    model= uploads
    context_object_name="profiles"
