"""proyectoTaller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from alumnos.models import detalle_boleta
from alumnos.views import agregar_producto, detallecarrito, elimina_producto, generarBoleta, limpiar_producto, restar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar/<str:codigo>/', agregar_producto, name='agregar_producto'),
    path('eliminar/<str:codigo>/', elimina_producto, name="elimina_producto"),
    path('restar/<str:codigo>/', restar_producto, name="restar_producto"),
    path('limpiar/', limpiar_producto, name='limpiar_producto'),
    path('detalle_boleta/', detalle_boleta, name='detalle_boleta'), 
    path('generarBoleta/', generarBoleta, name='generarBoleta'), 
    path('detallecarrito', detallecarrito, name='detallecarrito'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

