from django.contrib import admin
from .models import Marca, Productos, Contacto,Carrito

# Register your models here.
admin.site.register(Marca)
admin.site.register(Productos)
admin.site.register(Contacto)
admin.site.register(Carrito)

