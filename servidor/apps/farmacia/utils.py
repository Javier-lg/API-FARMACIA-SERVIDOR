from concurrent.futures import ThreadPoolExecutor
from apps.sincronizador.services import enviar_actualizacion_farmacia
from datetime import datetime
from apps.clientes.models import Cliente


def notificar_actualizacion(payload):
    fecha_de_actualizacion = datetime.now()

    def notificar_cliente(Cliente):
        return enviar_actualizacion_farmacia(fecha_de_actualizacion,Cliente,payload)

    with ThreadPoolExecutor(max_workers=2) as executor:  #hilos
        clientes = Cliente.objects.all()
        futures = {executor.submit(notificar_cliente, cliente): cliente for cliente in clientes}

        for future in futures:
            cliente = futures[future]
            try:
                resultado = future.result()
                print(f"Notificacion a {cliente.nombre}")
            except Exception as e:
                print(f"Error al notificar a {cliente.nombre} : {e}")
