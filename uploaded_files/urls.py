from django.urls import path
from . import views


urlpatterns  = [
    path('upload_project/<str:profile>', views.upload),
    path('project/<int:project_id>', views.displayproject)
]