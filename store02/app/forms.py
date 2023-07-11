from django import forms
from .models import Contacto,Productos,Carrito


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields= ["correo","contrasena"]
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Productos
        fields ="__all__"

class AgregarCarrito(forms.ModelForm):
    
    class Meta:
        model = Carrito
        fields ="__all__"
