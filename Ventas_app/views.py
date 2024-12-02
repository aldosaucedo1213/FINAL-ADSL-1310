from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_producto = request.POST["txtid_producto"]
    id_cliente = request.POST["txtid_cliente"]
    metodo_pago = request.POST["txtmetodo_pago"]
    fecha = request.POST["txtfecha"]
    id_empleado = request.POST["txtid_empleado"]
    total = request.POST["txttotal"]

    guardarventa = Ventas.objects.create(
        id_venta=id_venta,
        id_producto=id_producto,
        id_cliente=id_cliente,
        metodo_pago=metodo_pago,
        fecha=fecha,
        id_empleado=id_empleado,
        total=total
    )  # Guarda el registro

    return redirect("inicio_vistaVentas")

def seleccionarVenta(request, id_venta):
    lasventas = Ventas.objects.get(id_venta=id_venta)
    return render(request, "editarVentas.html", {"misventas": lasventas})

def editarVenta(request):
    id_venta = request.POST["txtid_venta"]
    id_producto = request.POST["txtid_producto"]
    id_cliente = request.POST["txtid_cliente"]
    metodo_pago = request.POST["txtmetodo_pago"]
    fecha = request.POST["txtfecha"]
    id_empleado = request.POST["txtid_empleado"]
    total = request.POST["txttotal"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_producto = id_producto
    venta.id_cliente = id_cliente
    venta.metodo_pago = metodo_pago
    venta.fecha = fecha
    venta.id_empleado = id_empleado
    venta.total = total
    venta.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaVentas")

def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.delete()  # Borra el registro
    return redirect("inicio_vistaVentas")
