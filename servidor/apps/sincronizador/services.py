import requests
from apps.clientes.models import Token


def enviar_actualizacion_farmacia(Cliente, payload):
    url = Cliente.direccion()
    token = Token.objects.get(Cliente=Cliente)
    headers = {
        "SAFESA-Token": str(token.key),
        "Content-Type": "application/json",
    }

    try:
        response = request.post(url, json=payload, headers = headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al informar la ultima actualizacion a {Cliente.nombre}: {e}")
        return {"error":str(e)}
    

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