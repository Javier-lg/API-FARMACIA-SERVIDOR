from rest_framework.permissions import IsAuthenticated #permiso
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.clientes.models import Cliente, Token

class registrarClienteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Obtén los datos de la solicitud
        nombre = request.data.get("nombre")
        descripcion = request.data.get("descripcion")
        host = request.data.get("host")
        url = request.data.get("url")
        base = request.data.get("base")
        port = request.data.get("port")

        # Validación de campos
        error = {}
        if not nombre:
            error["nombre_error"] = "Se requiere un nombre."
        if not host:
            error["host_error"] = "Se requiere un host."
        if not url:
            error["url_error"] = "Se requiere una URL."
        if not base:
            error["base_error"] = "Se requiere una base."
        if not port:
            error["port_error"] = "Se requiere un puerto."
        
        if error:
            return Response({"errors": error}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si ya existe un cliente con el mismo nombre
        cliente_existente = Cliente.objects.filter(nombre=nombre).first()
        if cliente_existente:
            token = Token.objects.get(Cliente=cliente_existente)
            return Response({
                "message": "El cliente ya está registrado.",
                "token": str(token.key)
            }, status=status.HTTP_200_OK)

        # Intentar crear el cliente
        try:
            cliente = Cliente.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                host=host,
                url=url,
                base=base,
                port=port
            )
            token = Token.objects.get(Cliente=cliente)
            return Response({
                "message": "Cliente creado exitosamente.",
                "token": str(token.key)
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "Ocurrió un error al crear el cliente.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
