from django.urls import path
from .views import (
    home,
    productos,
    carrito,
    ultimouser,
    iniciosesion,
    registro,
    agregar_producto,
    prueba,
    listar_productos,
    modificar_producto,
    eliminar_producto,
    agregar_carrito,
    eliminar_producto_carrito,
    limpiar_carrito,
    )

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('ultimouser/', ultimouser, name="ultimouser"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('registro/', registro, name="registro"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('prueba/',prueba, name = "prueba"),
    path('listar-productos/',listar_productos, name = "listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('eliminar-producto-carrito/<id>/', eliminar_producto_carrito, name="eliminar_producto_carrito"),
    path('agregar_carrito/', agregar_carrito, name='agregar_carrito'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito')
]