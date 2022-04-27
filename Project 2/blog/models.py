
from django.utils.text import slugify
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname()    


class Post(models.Model):
    title=models.CharField(max_length=100)
    image_name=models.CharField(max_length=100)          
    date = models.DateField(auto_now=True)
    excerpt=models.CharField(max_length=200)
    content=models.TextField(validators=[MinLengthValidator(10)])
    slug=models.SlugField(unique=True,db_index=True)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL ,null=True, related_name="posts")
    tag=models.ManyToManyField(Tag)


    def __str__(self):
        return f"{self.title,self.date,self.excerpt}"


class Comment(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField(max_length=120)
    post=models.ForeignKey( Post,on_delete=models.CASCADE,related_name="comments")
    
