from django.forms import ModelForm
from .models import Comment

class Comment_form(ModelForm):
    class Meta:
        model=Comment
        exclude=['post']
        labels={
            "username":"Your Name",
            "email":"Your Email",
            "comment":"Your Comment"
        }