from django.db import models

# Create your models here.

class Accionista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    rut = models.CharField(max_length=10, null=False)
    observacion = models.CharField(max_length=50, null=False)
    fecha_asociacion = models.DateField(null=False)
    activo = models.BooleanField(null=False)
    monto = models.IntegerField(null=False)

    def __str__(self):
            return str(self.id) + " " + self.nombre + " " + str(self.fecha_asociacion)
