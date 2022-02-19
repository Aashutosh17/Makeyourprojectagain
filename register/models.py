from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user =  models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null= True, unique=True)
    bio = models.TextField(max_length=500, blank=True , null= True)
    email = models.EmailField(max_length=100, blank=True , null=True)
    country = models.CharField(max_length=100, blank= True , null=True)
    profile_pic = models.ImageField(upload_to='images',default="/images/default.jpg", null=True, blank=True)

    def __str__(self):
        return self.name