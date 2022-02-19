from django import urls
from django.urls import path
from login import views

urlpatterns = [
    path('' , views.loginfn , name = 'login'),
    path('validation',views.validation),
    path('dashboard', views.dashboard),
    path('login_redirect', views.login_redirect),
    path('logout' , views.logoutfn)
]
