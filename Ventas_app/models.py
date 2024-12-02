from django.db import models

class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_producto = models.IntegerField(max_length=6)
    id_cliente = models.IntegerField(max_length=6)  # Corregido
    metodo_pago = models.CharField(max_length=100)  # Cambiado a CharField
    fecha = models.DateField(max_length=100)
    id_empleado = models.CharField(max_length=6)
    total = models.CharField(max_length=100)
    

    def __str__(self):
        return self.fecha
