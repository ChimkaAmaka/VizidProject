
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Comment(models.Model): 
   # post = models.ForeignKey(Post,
                            # on_delete=models.CASCADE,
                             #related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
class room(models.Model):
   name = models.CharField(max_length=30)
   feature= models.TextField(max_length=200)
