from django.db import models
from apps.clientes.models import Cliente

# Create your models here.

class ColaActualizaciones(models.Model):
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="tareas_pendientes")
    body = models.TextField()
    estado = models.CharField(max_length=50, choices=(("pendiente","Pendiente"), ("procesada","Procesada")))
    fecha_procesamiento = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Tarea Pendiente"
        verbose_name_plural = "Tareas Pnedientes"
        ordering = ["timestamp_actualizacion"]

class HistorialActualizaciones(models.Model):
    fecha_actualizacion = models.DateTimeField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ultima_actualizacion")