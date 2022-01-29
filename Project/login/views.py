import email
from register.models import registration
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorater import allowed_users

# Create your views here.
def login_redirect(request):
    return render(request, 'login.html')

@login_required(login_url='/login/login_redirect')
def dashboard(request):
    datas = registration.objects.all()
    return render(request , 'dashboard.html', {'datas': datas})

def validation(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/login/dashboard')
    else:
        messages.warning(request, 'Invalid Email or Password!')
        return redirect('/login/login_redirect')

def loginfn(request):
    if request.user.is_authenticated:
        return redirect('/login/dashboard')
    else:
        return render(request, 'login.html')

def logoutfn(request):
    logout(request)
    return redirect('/login/login_redirect')