
from django.forms import forms, models
from .models import registration
from django import forms

class user_information(forms.ModelForm):
    class Meta:
        model = registration
        fields = "__all__"