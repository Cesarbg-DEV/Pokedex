from django import forms
from django.forms import fields
from .models import Pokemon

class Pokemon_form(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('__all__')