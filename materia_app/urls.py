from django.urls import path
from producto_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarproducto/", views.registrarproducto, name="registrarproducto"),
    path("seleccionarproducto/<codigo>",views.seleccionarproducto,name="seleccionarproducto"),
    path("editarproducto/",views.editarproducto, name="editarproducto"),
    path("borrarproducto/<codigo>",views.borrarproducto, name="borrarproducto"),
    
]

