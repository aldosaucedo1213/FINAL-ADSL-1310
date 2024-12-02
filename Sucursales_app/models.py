from django.db import models

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)  # Corregido
    telefono = models.CharField(max_length=15)  # Cambiado a CharField
    horario = models.CharField(max_length=100)
    gerente = models.CharField(max_length=100)
    administrador = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
