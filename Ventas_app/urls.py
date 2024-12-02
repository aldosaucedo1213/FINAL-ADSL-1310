from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaVentas", views.inicio_vistaVentas, name="inicio_vistaVentas"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<id_venta>", views.seleccionarVenta, name="seleccionarVenta"),
    path("editarVenta/", views.editarVenta, name="editarVenta"),
    path("borrarVenta/<id_venta>", views.borrarVenta, name="borrarVenta"),
]
