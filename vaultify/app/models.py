from django.db import models

# Create your models here.
class Images(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

class Video(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)  

class Audio(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)         