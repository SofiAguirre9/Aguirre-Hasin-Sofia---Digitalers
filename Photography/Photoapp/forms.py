from django import forms 
from .models import Photo
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario para Subir Fotos 

class PhotoForm(forms.ModelForm):

    class Meta:
        model= Photo
        fields = ['name', 'description', 'rating', 'genders', 'Author', 'image', 'year']
        RATING = [
            (1, "Pricipiante"),
            (2, "Intermedio"),
            (3, "Avanzado"),
            (4, "Experto"),
            (5, "Profesional") ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Foto'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción'}),
            'rating': forms.Select(attrs={'class':'form-control', 'placeholder':'Nivel'}),
            'genders': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Géneros'}),
            'Author': forms.Select(attrs={'class':'form-control', 'placeholder':'Fotógrafo'}),
            'year': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Año de Captura'}),
        }

        labels = {
            'name' : "",
            'description': ""
        }

    def clean_year(self):
        anio = self.cleaned_data['year']
        if anio < 1970:
            raise ValidationError(("Error: No contiene la calidad minima solicitada"))
        return anio 

# Formulario para Crear Usuarios

class UsuariosForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un usuario'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Reescribe la contraseña'}))
    Publicar_Fotos = forms.BooleanField()

    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2', 'Publicar_Fotos']