from .models import ColaActualizaciones, SeguimientoActualizaciones

def actualizacion_pendiente(Cliente, payload, fecha):
    ColaActualizaciones.objects.create(
        fecha_actualizacion = fecha,
        Cliente = Cliente,
        payload = payload,
        estado = 'pendiente',
        fecha_procesamiento = None
    )

def actualizar_historial(fecha,Cliente):
    seguimiento = SeguimientoActualizaciones.objects.get_or_create(
        Cliente = Cliente
    )
    seguimiento.fecha_actualizacion = fecha
    seguimiento.save()