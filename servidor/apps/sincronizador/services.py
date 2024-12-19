import requests # type: ignore
from apps.clientes.models import Token


import requests  # type: ignore
from apps.clientes.models import Token

def enviar_actualizacion_farmacia(cliente, timestamp, payload):
    url = cliente.direccion()
    token = Token.objects.get(cliente=cliente) 
    headers = {
        "SAFESA-Token": str(token.key),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # si el codigo de estado no indica exito (>=400)
        return {
            "status": "success",
            "status_code": response.status_code,
            "response": response.json(),
            "error": None,
        }
    except requests.exceptions.RequestException as e:
        # errores
        return {
            "status": "failed",
            "status_code": getattr(e.response, "status_code", None),  #  codigo de estado si esta disponible
            "response": None,
            "error": str(e),
        }
    

    '''
from apps.sincronizador.services import informar_cliente
from apps.clientes.models import Cliente

# Obtener el cliente
cliente = Cliente.objects.get(nombre="Cliente1")

# Datos de la actualización
data = {"tipo": "actualizacion", "detalle": "Se modificó el inventario"}

# Informar al cliente
respuesta = informar_cliente(cliente, data)
print(respuesta)

    '''