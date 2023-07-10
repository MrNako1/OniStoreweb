from django.urls import path
from .views import home,productos,carrito,ultimouser,iniciosesion,registro,agregar_producto,prueba

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('carrito/', carrito, name='carrito'),
    path('ultimouser/', ultimouser, name='ultimouser'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('registro/', registro, name='registro'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('prueba/',prueba, name = 'prueba'),
]
