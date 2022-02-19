from django.urls import path
from . import views

urlpatterns  = [
    path('<str:profilename>', views.profile)
]