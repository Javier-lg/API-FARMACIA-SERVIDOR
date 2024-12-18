# clientes/urls.py
from django.urls import path
from .views import registrarClienteView

urlpatterns = [
    path('registrar_cliente/', registrarClienteView.as_view(), name='registrar_cliente'),
]
