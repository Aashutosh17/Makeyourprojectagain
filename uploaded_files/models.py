from django.db import models


# Create your models here.
class uploaded(models.Model):
    uploaded_by = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=400,blank=True,null=True)
    image = models.ImageField(upload_to = 'images' , blank=True, null=True)
    links = models.URLField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    profile_image = models.ImageField(default= "images/default.jpg",blank =True, null= True)
    project_title = models.CharField(max_length=200,blank=True,null=True)