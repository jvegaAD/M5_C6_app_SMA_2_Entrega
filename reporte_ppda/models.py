# reporte_ppda/models.py

from django.db import models

class Organismo(models.Model):
    nombre = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    correo_contacto = models.EmailField()

    def __str__(self):
        return self.nombre


class MedidaPPDA(models.Model):
    TIPO_CHOICES = [
        ('regulatoria', 'Regulatoria'),
        ('no_regulatoria', 'No Regulatoria'),
    ]

    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    indicador = models.CharField(max_length=255)
    medio_verificacion = models.TextField()
    organismo_responsable = models.ForeignKey(Organismo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class AvanceMedida(models.Model):
    medida = models.ForeignKey(MedidaPPDA, on_delete=models.CASCADE)
    fecha_reporte = models.DateField()
    porcentaje_avance = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True)
    archivo_respaldo = models.FileField(upload_to='reportes/', null=True, blank=True)

    def __str__(self):
        return f"{self.medida.nombre} - {self.fecha_reporte}"
