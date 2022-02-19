from django import forms
from register.models import UserProfile

class profile_register(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = "__all__"
        exclude = ['user']