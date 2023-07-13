
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio ),
    path('gestion', views.gestion, name='gestion'),
    path('Inicio', views.Inicio, name='Inicio'),
    path('mecanicos', views.mecanicos, name='mecanicos'),
    path('promociones', views.promociones, name='promociones'),
    path('servicios', views.servicios, name='servicios'),
    path('suscribirse', views.suscribirse, name='suscribirse'),
    path('registrar/',views.registrar, name='registrar'), 
    path('edicion/<rut>', views.edicion, name='edicion'),  
    path('editar/', views.editar, name='editar'), 
    path('eliminar/<rut>', views.eliminar, name='eliminar'),  
    path('home', views.home, name='home'),
    path('logout/', views.exit, name='exit'),
    path('tienda/', views.tienda, name='tienda'), 
    path('generarBoleta/', views.generarBoleta, name='generarBoleta'),   
    path('agregar/<str:codigo>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<str:codigo>/', views.elimina_producto, name="elimina_producto"),
    path('restar/<str:codigo>/', views.restar_producto, name="restar_producto"),
    path('limpiar/', views.limpiar_producto, name='limpiar_producto'),
    
    
    
]



