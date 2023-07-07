from django.shortcuts import render,redirect 
from .models import Cliente 
from django.contrib import messages

# Create your views here.


def Inicio(request):
    context ={}
    return render(request, 'alumnos/Inicio.html')

def mecanicos(request):
    context ={}
    return render(request, 'alumnos/mecanicos.html')

def promociones(request):
    context ={}
    return render(request, 'alumnos/promociones.html')

def servicios(request):
    context ={}
    return render(request, 'alumnos/servicios.html')

def suscribirse(request):
    context ={}
    return render(request, 'alumnos/suscribirse.html')

def gestion(request):
    listadoClientes = Cliente.objects.all()
    return render(request, 'alumnos/gestion.html', {"clientes" : listadoClientes })

def registrar(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellidoP=request.POST['txtApellidoP']
    apellidoM=request.POST['txtApellidoM']

    cliente = Cliente.objects.create(
        rut=rut , nombre=nombre, apellido_paterno=apellidoP, apellido_materno=apellidoM)
    return redirect('gestion')

def edicion(request, rut):
    cliente = Cliente.objects.get(rut = rut)
    data={



    }
    return render(request,'alumnos/edicion.html', {"cliente": cliente})

def editar(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido_paterno = request.POST['apellido_paterno']
    apellido_materno = request.POST['apellido_materno']

    cliente = Cliente.objects.get(rut = rut)
    cliente.rut = rut
    cliente.nombre = nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.save()
    return redirect('gestion')



def eliminar(request, rut):
    cliente= Cliente.objects.get(rut=rut)
    cliente.delete()
    return redirect('gestion')

    