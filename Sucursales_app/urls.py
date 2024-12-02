from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaSucursal", views.inicio_vistaSucursal, name="inicio_vistaSucursal"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal"),
    path("borrarSucursal/<id_sucursal>", views.borrarSucursal, name="borrarSucursal"),
]
