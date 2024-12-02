from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)  # Corregido
    correo_electronico = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)  # Cambiado a CharField
    tipo_cliente = models.CharField(max_length=100)
    metodo_de_pago = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
