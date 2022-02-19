from curses.ascii import US
from unicodedata import name
from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import  Registerform
from .models import UserProfile
from django.contrib.auth.models import User


# Create your views here.

# def add_user(request):
#     print("1")
#     if (request.method == "POST"):
#         print("2")
#         form = user_information(request.POST, request.FILES)

#         form.save()

#         messages.success(request, 'Successfully Registered')
#         return redirect('/login/login_redirect')
#     else:
#         print("3")
#         form = user_information()
#         return redirect(request, '/register', {'form': form})


def registration(request):
    form = Registerform()

    if (request.method == "POST"):
        form = Registerform(request.POST)

        if(form.is_valid()):

            user = form.save()
            UserProfile.objects.create(
                user=user, name=user.username, email = user.email
            )
            return redirect('/login/login_redirect')
        else:
            return HttpResponse('form didnot save!')
    else:

        return render(request , 'registration_2.html' , {'form' : form})