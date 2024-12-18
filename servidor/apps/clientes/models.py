import uuid
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    host = models.CharField(max_length=25)
    url = models.CharField(max_length=25)
    base = models.CharField(max_length=25)
    port = models.CharField(max_length=6)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def direccion(self):
        return f"{self.host}:{self.port}/{self.base}/{self.url}"
    
    @property
    def is_authenticated(self):
        return True
    
class Token(models.Model):
    Cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name="secure_token")
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return str(self.key)