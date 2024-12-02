from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.
def inicio_vistaSucursal(request):
    lassucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursales.html", {"missucursales": lassucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtid_sucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    horario = request.POST["txthorario"]
    gerente = request.POST["txtgerente"]
    administrador = request.POST["txtadministrador"]

    guardarsucursal = Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        horario=horario,
        gerente=gerente,
        administrador=administrador
    )  # Guarda el registro

    return redirect("inicio_vistaSucursal")

def seleccionarSucursal(request, id_sucursal):
    lassucursales = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursales.html", {"missucursales": lassucursales})

def editarSucursal(request):
    id_sucursal = request.POST["txtid_sucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    horario = request.POST["txthorario"]
    gerente = request.POST["txtgerente"]
    administrador = request.POST["txtadministrador"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.telefono = telefono
    sucursal.horario = horario
    sucursal.gerente = gerente
    sucursal.administrador = administrador
    sucursal.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaSucursal")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()  # Borra el registro
    return redirect("inicio_vistaSucursal")
