from django.db import models

# Create your models here.

class ServidoresRemotos(models.Model):
    nombrehospital = models.CharField(blank=True, null=True)
    direccionip = models.CharField(blank=True, null=True)
    puerto = models.CharField(blank=True, null=True)
    usuario = models.CharField(blank=True, null=True)
    clave = models.CharField(blank=True, null=True)
    estado = models.CharField(blank=True, null=True)
    tiempo_demora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidores_remotos'


class TmEstablecimientos(models.Model):
    tmestablecimientoid = models.IntegerField(primary_key=True)
    tmestablecimientonombre = models.CharField(max_length=120, blank=True, null=True)
    tmcodigorefes = models.CharField(max_length=120, blank=True, null=True)
    tmhistoriaclinicaelectronica = models.CharField(max_length=120, blank=True, null=True)
    tmtipoestablecimiento = models.CharField(max_length=120, blank=True, null=True)
    tmmunicipio = models.CharField(max_length=120, blank=True, null=True)
    tmdepartamento = models.CharField(max_length=120, blank=True, null=True)
    tmprovincia = models.CharField(max_length=120, blank=True, null=True)
    tmzonaoperativa = models.CharField(max_length=120, blank=True, null=True)
    tmdescripcion = models.CharField(max_length=120, blank=True, null=True)
    tmareanumero = models.CharField(max_length=120, blank=True, null=True)
    tmareaoperativa = models.CharField(max_length=120, blank=True, null=True)
    tmubicacioncodigointerno = models.CharField(max_length=40, blank=True, null=True)
    tmubicacioncodigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_establecimientos'