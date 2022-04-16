
from django.db import models

# Create your models here.
class Review(models.Model):
    user_name=models.CharField(max_length=100)
    text_area=models.TextField(max_length=500)
    rating=models.IntegerField()
