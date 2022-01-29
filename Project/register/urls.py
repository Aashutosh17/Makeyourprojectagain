from django import urls
from django.urls import path
from register import views

urlpatterns = [
    path('' , views.registration),
    path('add_user', views.add_user)
]
