from django.db import models
from apps.clientes.models import Cliente

# Create your models here.

class ColaActualizaciones(models.Model):
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="tareas_pendientes")
    payload = models.TextField()
    estado = models.CharField(max_length=50, choices=(("pendiente","Pendiente"), ("procesada","Procesada")))
    fecha_procesamiento = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Tarea Pendiente"
        verbose_name_plural = "Tareas Pnedientes"
        indexes = [
            models.Index(fields=["Cliente"]),
            models.Index(fields=["estado"]),
            models.Index(fields=["fecha_procesamiento"]),
        ]

class SeguimientoActualizaciones(models.Model):
    Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE,primary_key=True, related_name="ultima_actualizacion")
    fecha_actualizacion = models.DateTimeField()
    