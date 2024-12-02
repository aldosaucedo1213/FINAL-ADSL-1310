from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    curp=request.POST["txtcurp"]
    telefono=request.POST["numtelefono"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    email=request.POST["txtemail"]
    fechadeingreso=request.POST["txtfechadeingreso"]
    guardarempleado=Empleado.objects.create(
        id_empleado=id_empleado,curp=curp,telefono=telefono,nombre=nombre,apellido=apellido,direccion=direccion,email=email,fechadeingreso=fechadeingreso
    )#Guarda el registro

    return redirect("inicio_vistaEmpleado")
def seleccionarEmpleado(request,id_empleado):
    losempleados=Empleado.objects.get(id_empleado=id_empleado)
    fecha=losempleados.fechadeingreso.strftime('%Y-%m-%d')
    return render(request,"editarEmpleado.html", {"misempleados":losempleados,"misempleados":losempleados,"fecha":fecha})

def editarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    curp=request.POST["txtcurp"]
    telefono=request.POST["numtelefono"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    email=request.POST["txtemail"]
    fechadeingreso=request.POST["txtfechadeingreso"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.curp=curp
    empleado.telefono=telefono
    empleado.nombre=nombre
    empleado.apellido=apellido
    empleado.direccion=direccion
    empleado.email=email
    empleado.fechadeingreso=fechadeingreso
    empleado.save()#guarda registro actualizado
    return redirect("inicio_vistaEmpleado")


def borrarEmpleado(request, id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete() # borra el registro
    return redirect("inicio_vistaEmpleado")

    
