from django.shortcuts import render, redirect
from .models import producto

# Create your views here.
def inicio_vista(request):
    lasproductos=producto.objects.all()
    return render(request,"gestionarproducto.html",{"misproductos":lasproductos})

def registrarproducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarproducto=producto.objects.create(
        codigo=codigo, nombre=nombre,creditos=creditos
    )#Guarda el registro

    return redirect("/")
def seleccionarproducto(request,codigo):
    producto=producto.objects.get(codigo=codigo)
    return render(request,"editarproducto.html", {"misproductos":producto})

def editarproducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    producto=producto.objects.get(codigo=codigo)
    producto.nombre=nombre
    producto.creditos=creditos
    producto.save()#guarda registro actualizado
    return redirect("/")


def borrarproducto(request, codigo):
    producto=producto.objects.get(codigo=codigo)
    producto.delete() # borra el registro
    return redirect("/")

    
