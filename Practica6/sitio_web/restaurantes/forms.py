from django import forms
from django.core.validators import RegexValidator

class SearchForm(forms.Form):
    auto_id = False
    restaurante = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control mr-sm-2 mb-2 mb-sm-0',
            'placeholder':'Buscar..'
        }
    ), label='')

class AddFormRestaurant(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Ingrese el nombre',
            }
        ),
        max_length=100,
        validators=[
            RegexValidator(r'^\D+$', message="El nombre no debe contener dígitos")
        ]
    )

    locationx = forms.FloatField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Latitud',
            }
        ),
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )

    locationy = forms.FloatField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Longitud',
            }
        ),
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )

class ModifyFormRestaurant(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
            'class':'form-control',
            }
        ),
        max_length=100,
        validators=[
            RegexValidator(r'^\D+$', message="El nombre no debe contener dígitos")
        ]
    )

    locationx = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 10,
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )

    locationy = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 10,
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )

class AddFormPlate(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 100,
        validators=[
            RegexValidator(r'^\D+$', message="El nombre no debe contener dígitos")
        ]
    )

    tipocomida = (
                    ("Americana", "Americana"),
                    ("China", "China"),
                    ("Española", "Española"),
                    ("Italiana", "Italiana"),
                    ("Japonesa", "Japonesa"),
                    ("Turca", "Turca"),
                    ("Alemana", "Alemana"),
                    ("Andaluza", "Andaluza"),
                    ("Arabe", "Arabe"),
                    ("Argentina", "Argentina"),
                    ("Brasileña", "Brasileña"),
                    ("Casera", "Casera"),
                    ("Colombiana", "Colombiana"),
                    ("Hawainana", "Hawaiana"),
                    ("Mexicana", "Mexicana"),
                    ("Oriental", "Oriental"),
                    ("Peruana", "Peruana"),
                    ("Tailandesa", "Tailandesa"),
                    ("Vegana", "Vegana"),
                    ("Vegetariana", "Vegetariana")
                )

    tipocomida = forms.ChoiceField(widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ),
        choices=tipocomida
    )

    alergenos = (   
                    ("Contiene Gluten", "Contiene Gluten"), 
                    ("Crustáceno", "Crustáceno"), 
                    ("Huevos", "Huevos"), 
                    ("Pescado", "Pescado"), 
                    ("Cacahuete", "Cacahuete"), 
                    ("Soja", "Soja"), 
                    ("Lacteos", "Lacteos"), 
                    ("Frutos de cascara", "Frutos de cascara"), 
                    ("Apio", "Apio"), 
                    ("Mostaza", "Mostaza"), 
                    ("Granos de sesamo", "Granos de sesamo"), 
                    ("Dióxido de azufre y sulfitos", "Dióxido de azufre y sulfitos"), 
                    ("Moluscos", "Moluscos"), 
                    ("Altramuce", "Altramuces"), 
                )

    alergenos = forms.MultipleChoiceField(widget=forms.SelectMultiple(
            attrs={
                'class':'form-control'
            }
        ),
        choices=alergenos
    )


    precio = forms.FloatField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )

class ModifyFormPlate(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        max_length = 100,
        validators=[
            RegexValidator(r'^\D+$', message="El nombre no debe contener dígitos")
        ]
    )

    tipocomida = (
                    ("Americana", "Americana"),
                    ("China", "China"),
                    ("Española", "Española"),
                    ("Italiana", "Italiana"),
                    ("Japonesa", "Japonesa"),
                    ("Turca", "Turca"),
                    ("Alemana", "Alemana"),
                    ("Andaluza", "Andaluza"),
                    ("Arabe", "Arabe"),
                    ("Argentina", "Argentina"),
                    ("Brasileña", "Brasileña"),
                    ("Casera", "Casera"),
                    ("Colombiana", "Colombiana"),
                    ("Hawainana", "Hawaiana"),
                    ("Mexicana", "Mexicana"),
                    ("Oriental", "Oriental"),
                    ("Peruana", "Peruana"),
                    ("Tailandesa", "Tailandesa"),
                    ("Vegana", "Vegana"),
                    ("Vegetariana", "Vegetariana")
                )

    tipocomida = forms.ChoiceField(widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ),
        choices=tipocomida
    )

    alergenos = (   
                    ("Contiene Gluten", "Contiene Gluten"), 
                    ("Crustáceno", "Crustáceno"), 
                    ("Huevos", "Huevos"), 
                    ("Pescado", "Pescado"), 
                    ("Cacahuete", "Cacahuete"), 
                    ("Soja", "Soja"), 
                    ("Lacteos", "Lacteos"), 
                    ("Frutos de cascara", "Frutos de cascara"), 
                    ("Apio", "Apio"), 
                    ("Mostaza", "Mostaza"), 
                    ("Granos de sesamo", "Granos de sesamo"), 
                    ("Dióxido de azufre y sulfitos", "Dióxido de azufre y sulfitos"), 
                    ("Moluscos", "Moluscos"), 
                    ("Altramuce", "Altramuces"), 
                )

    alergenos = forms.MultipleChoiceField(widget=forms.SelectMultiple(
            attrs={
                'class':'form-control'
            }
        ),
        choices=alergenos
    )


    precio = forms.FloatField(widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        validators=[
            RegexValidator(r'\d+$', message="El campo debe de contener numeros")
        ]
    )