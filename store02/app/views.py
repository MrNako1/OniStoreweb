from django.shortcuts import render
from .models import Productos
from .forms import ContactoForm, ProductoForm


# Create your views here.

def home(request):
    return render(request,'app/home.html')

def productos(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/productos.html',data)

def carrito(request):
    return render(request,'app/carrito.html')

def registro(request):
    data ={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "guardado correctamente"
            
        else:
            data["form"]= formulario        
    return render(request,'app/registro.html',data)

def ultimouser(request):
    return render(request,'app/ultimouser.html')

def iniciosesion(request):
    return render(request,'app/iniciosesion.html')


def agregar_producto(request):
    data = {
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    

    return render(request,'app/newproducto/agregar.html', data)


def prueba(request):
    return render(request, 'app/prueba.html')