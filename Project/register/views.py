from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import user_information


# Create your views here.

def add_user(request):
    print("1")
    if (request.method == "POST"):
        print("2")
        form = user_information(request.POST, request.FILES)

        form.save()

        messages.success(request, 'Successfully Registered')
        return redirect('/login/login_redirect')
    else:
        print("3")
        form = user_information()
        return redirect(request, '/register', {'form': form})


def registration(request):
    return render(request , 'registration_2.html')