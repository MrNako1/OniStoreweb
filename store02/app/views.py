from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


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

@permission_required('app.add_prodcuto')
def agregar_producto(request):
    data = {
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "agregado correctamente")
        else:
            data["form"] = formulario
    

    return render(request,'app/newproducto/agregar.html', data)


def prueba(request):
    return render(request, 'app/prueba.html')

@permission_required('app.view_prodcuto')
def listar_productos(request):
    productos = Productos.objects.all()

    data = {
        'productos' : productos
        }
    return render(request, 'app/newproducto/listar.html', data)

@permission_required('app.change_prodcuto')
def modificar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'app/newproducto/modificar.html', data)

@permission_required('app.delete_prodcuto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")

    return redirect(to="listar_productos") 

def registron(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registron.html', data)