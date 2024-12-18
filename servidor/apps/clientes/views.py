from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated #permiso
#from .authentication import TokenAuthentication
from .models import Cliente, Token

class registrarClienteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        nombre = request.data.get("nombre")
        descripcion = request.data.get("descripcion")
        host = request.data.get("host")
        url = request.data.get("url")
        base = request.data.get("base")
        port = request.data.get("port")

        error = {}

        if not nombre:
            error["nombre_error"] = "se requiere un nombre"
        if not host:
            error["host_error"] = "se requiere un host"
        if not url:
            error["url_error"] = "se requiere una url"
        if not base:
            error["base_error"] = "se requiere un base"
        if not port:
            error["port_error"] = "se requiere un puerto"
            
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
        cliente = Cliente.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            host=host,
            url=url,
            base=base,
            port=port
        )
        token = Token.objects.get(Cliente=cliente)

        return Response({"token": str(token.key)}, status=status.HTTP_200_OK)