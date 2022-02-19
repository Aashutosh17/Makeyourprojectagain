from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from register.models import UserProfile 
from uploaded_files.models import uploaded

# Create your views here.
def login_redirect(request):
    return render(request, 'login.html')


# --------------------------- Dashboard ------------------------------------
@login_required(login_url='/login/login_redirect')
def dashboard(request):
    datas = UserProfile.objects.all()
    profile = UserProfile.objects.get(name = request.user.username)
    total_uploads = uploaded.objects.all()

    return render(request , 'dashboard.html', {'datas': datas , 'pic': profile, 'uploaded': total_uploads})

# --------------------------- Validation ------------------------------------
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


# --------------------------- Login ------------------------------------
def loginfn(request):
    if request.user.is_authenticated:
        return redirect('/login/dashboard')
    else:
        return render(request, 'login.html')


# --------------------------- Logout ------------------------------------
def logoutfn(request):
    logout(request)
    return redirect('/login/login_redirect')