from typing import Text
from django.forms import ModelForm, TextInput, widgets
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City Name'})}