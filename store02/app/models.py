from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre



class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="objetos", null=True)
    

    def __str__(self):
        return self.nombre
    
class Contacto (models.Model):
    correo=models.EmailField()
    contrasena=models.CharField(max_length=6)
    
    def __str__(self):
        return self.correo
        
       
    


