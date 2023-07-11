from django import forms
from .models import Contacto,Productos
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
    correo = forms.CharField(min_length=5)
    contrasena=forms.CharField(min_length=6)

    class Meta:
        model = Contacto
        #fields= ["correo","contrasena"]
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    precio=forms.IntegerField(min_value=30000, max_value=10000000)
    nombre=forms.CharField(min_length=5)
    imagen = forms.ImageField(required=False)
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Productos.objects.filter(nombre__iexact=nombre).exists()
        
        if existe:
            raise ValidationError("Este Nombre ya existe")
        return nombre
    

    
    class Meta:
        model = Productos
        fields ="__all__"

class CustomUserCreationForm(UserCreationForm):
    pass