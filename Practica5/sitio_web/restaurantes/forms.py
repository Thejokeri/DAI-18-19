from django import forms
from .models import Post
from django.core.validators import RegexValidator

class SearchForm(forms.Form):
    auto_id = False
    restaurante = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control mr-sm-2 mb-2 mb-sm-0',
            'placeholder':'Buscar..'
        }
    ), label='')

class AddForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Ingrese el nombre',
            }
        ),
        max_length=100
    )

    locationx = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Latitud',
            }
        ),
        max_length = 10
    )

    locationy = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Longitud',
            }
        ),
        max_length = 10
    )

class ModifyForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
            'class':'form-control',
            }
        ),
        max_length=100
    )

    locationx = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 10
    )

    locationy = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 10
    )