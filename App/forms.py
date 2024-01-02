from django import forms
from App.models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
