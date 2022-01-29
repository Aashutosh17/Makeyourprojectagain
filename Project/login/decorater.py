from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles = []):
    def decorater(view_func):
        def wrapper_func(request, *args , **kwargs):

            print('Working', allowed_roles)

            return view_func(request, *args , **kwargs)
        return wrapper_func
    return decorater