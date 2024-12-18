from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cliente, Token

@receiver(post_save, sender=Cliente)
def crear_token_dispositivo(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(Cliente=instance)