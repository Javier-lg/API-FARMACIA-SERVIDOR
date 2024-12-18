from django.contrib import admin
from .models import Cliente, Token

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Token)