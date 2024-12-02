from django.shortcuts import render, redirect
from .models import Cliente

# Vista para gestionar clientes
def gestionarCliente(request):
    misclientes = Cliente.objects.all()
    return render(request, 'gestionarCliente.html', {'misclientes': misclientes})

# Vista para registrar un nuevo cliente
def registrarCliente(request):
    if request.method == 'POST':
        id_cliente = request.POST['txtid_cliente']
        nombre = request.POST['txtnombre']
        direccion = request.POST['txtdireccion']
        correo_electronico = request.POST['txtemail']
        telefono = request.POST['numtelefono']
        tipo_cliente = request.POST['txttipo_cliente']
        metodo_de_pago = request.POST['txtmetodo_pago']

        # Crear el cliente en la base de datos
        Cliente.objects.create(
            id_cliente=id_cliente,
            nombre=nombre,
            direccion=direccion,
            correo_electronico=correo_electronico,
            telefono=telefono,
            tipo_cliente=tipo_cliente,
            metodo_de_pago=metodo_de_pago
        )
        return redirect('gestionarCliente')

    return render(request, 'registrarCliente.html')

# Vista para editar un cliente existente
def editarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.nombre = request.POST['txtnombre']
        cliente.direccion = request.POST['txtdireccion']
        cliente.correo_electronico = request.POST['txtemail']
        cliente.telefono = request.POST['numtelefono']
        cliente.tipo_cliente = request.POST['txttipo_cliente']
        cliente.metodo_de_pago = request.POST['txtmetodo_pago']
        cliente.save()
        return redirect('gestionarCliente')

    return render(request, 'editarCliente.html', {'cliente': cliente})

# Vista para borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('gestionarCliente')
