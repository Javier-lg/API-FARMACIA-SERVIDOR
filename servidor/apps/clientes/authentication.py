from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token_key = request.headers.get('SAFESA-Token')  #estandar es Authorization
        if not token_key:
            return None  

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Token inválido.")  

        if token.fecha_baja:
            raise AuthenticationFailed("El token está inactivo.")

        return (token.Cliente, None)



