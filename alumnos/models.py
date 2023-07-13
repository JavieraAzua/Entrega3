import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    rut              = models.CharField(primary_key=True,max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)


    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    
class Producto(models.Model):
    codigo= models.CharField(primary_key = True, max_length= 8)
    nombre_producto = models.CharField(max_length=60)
    imagen= models.ImageField(upload_to='imagenes', null= True, blank= True, verbose_name='imagen')
    precio=models.IntegerField(blank=True, null=True, verbose_name='Precio')

    def __str__(self):
        return str(self.nombre_producto)+" "+str(self.precio)
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()

    def __str__(self):
        return str(self.id_boleta)
    
class detalle_boleta(models.Model):
    id_boleta=models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta=models.AutoField(primary_key=True)
    codigo=models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    subtotal = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id_detalle_boleta)