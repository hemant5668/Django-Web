
from django import forms
from .models import Review



class Reviewforms(forms.Form):
    username=forms.CharField(max_length=100 ,error_messages={
        "max_length":"Please enter shorter length",
        "required":"Your name must required" 
    })
    feedback=forms.CharField(max_length=500, label="Your Feedback", widget=forms.Textarea)
    rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)


class Reviewforms1(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        labels={
            "user_name": "User Name",
            "text_area":"Feedback",
            "rating":"Rating"
        }
        error_messages={
            "user_name":{
                "max_length":"Please enter shorter length",
                "required":"Your name must required" 
            }
        } 
