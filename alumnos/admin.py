from django.contrib import admin
from .models import Boleta, Cliente, Producto, detalle_boleta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)



# Register your models here.
#admin.site.register(Genero)
#admin.site.register(Alumno)
#para crear mas tablas.... from .models import Cliente , genero , alumnos