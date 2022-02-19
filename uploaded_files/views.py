from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import upload_form
from register.models import UserProfile
from uploaded_files.models import uploaded

# Create your views here.
# Uploading page
@login_required(login_url='/login/login_redirect')
def upload(request, profile):
    user_profile = UserProfile.objects.get(name=profile)
    forms = upload_form()

    if(request.method == "POST"):
        form = upload_form(request.POST , request.FILES)
        
        if(form.is_valid()):
            form.save()
            return HttpResponse('saved')

        else:
            return HttpResponse('not saved')

    return render(request , 'uploadpage.html', {'profile': user_profile , 'form': forms})

@login_required(login_url='/login/login_redirect')
def displayproject(request , project_id):
    display_project = uploaded.objects.get(id = project_id)
    profile = UserProfile.objects.get(name= request.user.username)
    return render(request , 'displayproject.html' , {'project_detail': display_project , 'profile' : profile})




