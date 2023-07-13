from django.shortcuts import render,redirect , HttpResponse

from alumnos.compra import carrito
from .models import Boleta, Cliente, Producto, detalle_boleta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.

def home(request):
    context ={}
    return render(request, 'alumnos/home.html')

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

@login_required
def gestion(request):
    listadoClientes = Cliente.objects.all()
    return render(request, 'alumnos/gestion.html', {"clientes" : listadoClientes })

def exit(request):
    logout(request)
    return redirect('login')

@login_required
def registrar(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    apellidoP=request.POST['txtApellidoP']
    apellidoM=request.POST['txtApellidoM']

    cliente = Cliente.objects.create(
        rut=rut , nombre=nombre, apellido_paterno=apellidoP, apellido_materno=apellidoM)
    return redirect('gestion')

@login_required
def edicion(request, rut):
    cliente = Cliente.objects.get(rut = rut)
    return render(request,'alumnos/edicion.html', {"cliente": cliente})

@login_required
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

@login_required
def eliminar(request, rut):
    cliente= Cliente.objects.get(rut=rut)
    cliente.delete()
    return redirect('gestion')


def tienda(request):
    productos = Producto.objects.all()
    carrito_compra = carrito(request)
    total = sum(int(item['cantidad']) for item in carrito_compra.carrito.values())
    return render(request, 'alumnos/tienda.html', {'productos': productos, 'carrito': carrito_compra, 'total': total})

def agregar_producto(request,codigo):
	carrito_compra = carrito(request)
	producto = Producto.objects.get(codigo=codigo)
	carrito_compra.agregar(producto = producto)
	return redirect('tienda')

def elimina_producto(request, codigo):
	carrito_compra = carrito(request)
	producto = Producto.objects.get(codigo=codigo)
	carrito_compra.eliminar(producto=producto)
	return redirect('tienda')


def restar_producto(request, codigo):
	carrito_compra = carrito(request)
	producto = Producto.objects.get(codigo=codigo)
	carrito_compra.restar(producto=producto)
	return redirect('tienda')

def limpiar_producto(request):
    carrito_compra = carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')

def detallecarrito(request):
    context ={}
    return render(request, 'alumnos/detallecarrito.html')

def generarBoleta(request):
	precio_total= 0
	for key, value in request.session['carrito'].items():
		precio_total= precio_total + int(value['precio']) * int(value['cantidad'])
	boleta = Boleta(total= precio_total)
	boleta.save()
	productos= []
        #almacena la informacion en detalle de boleta
	for key, value in request.session['carrito'].items():
		producto= Producto.objects.get(codigo=value['codigo'])
		cant= value['cantidad']
		subtotal= cant * int(value['precio'])
		detalle= detalle_boleta(id_boleta= boleta, codigo= producto, cantidad= cant, subtotal= subtotal)
		detalle.save() #almacenamos un objeto en la base de datos
		productos.append(detalle) #
	datos={
		'productos': productos,
		'total': boleta.total 
	}
	request.session['boleta']= boleta.id_boleta
	carrito_instancia= carrito(request)
	carrito_instancia.limpiar()
	return render(request,'alumnos/detallecarrito.html',datos)



