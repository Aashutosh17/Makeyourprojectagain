
from .models import uploaded
from django import forms

class upload_form(forms.ModelForm):
    class Meta():
        model = uploaded
        fields = "__all__"