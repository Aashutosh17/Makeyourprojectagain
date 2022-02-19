from django.http import HttpResponse
from django.shortcuts import render
from register.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import profile_register
from register.models import UserProfile
from register.forms import Registerform
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/login_redirect')
def profile(request , profilename):
    user_profile = UserProfile.objects.get(name = profilename)
    user_email = User.objects.get(username = profilename)
    
    if (request.method == "POST"):
        user_upadte = UserProfile.objects.get(name=profilename)
        form = profile_register(request.POST , request.FILES, instance=user_upadte)

        if (form.is_valid()):
            form.save()
            return render(request , 'profile.html' , {'profiledata' : user_profile , 'user_email' : user_email})
        
        else:
            return HttpResponse('not done')

    
    user_profile = UserProfile.objects.get(name = profilename)
    user_email = User.objects.get(username = profilename)
    form = profile_register()

    return render(request , 'profile.html' , {'form': form,'profiledata' : user_profile , 'user_email' : user_email})