from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
import json
import psycopg2

class Command(BaseCommand):
    help = "Escucha cambios en la tabla 'tm_insumosmedicos' y genera le mensaje a enviar."

    def handle(self, *args, **kwargs):
        db_alias = "SAFESA_TM"  # base de datos registrada en settings/local.py
        connection = connections[db_alias]

        if connection.vendor != 'postgresql':
            self.stderr.write(self.style.ERROR("Esto solo funciona con PostgreSQL."))
            return

        self.stdout.write(self.style.SUCCESS(f"Conectando a la base de datos '{connection.settings_dict['NAME']}'..."))
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("LISTEN table_changes;")
                self.stdout.write(self.style.SUCCESS("Escuchando cambios en 'tm_insumosmedicos'..."))

                while True:
                    # Poll para recibir notificaciones
                    connection.connection.poll()

                    # Procesar notificaciones
                    while connection.connection.notifies:
                        notify = connection.connection.notifies.pop(0)
                        payload = json.loads(notify.payload)
                        self.stdout.write(self.style.SUCCESS(f"Operación: {payload['operation']}"))
                        self.stdout.write(f"Datos nuevos: {payload['data']}")
                        if 'old_data' in payload:
                            self.stdout.write(f"Datos antiguos: {payload['old_data']}")

                        if payload['operation'] == 'INSERT':
                            self.notificar_servidores(payload['operation'], payload['data'])
                        elif payload['operation'] == 'UPDATE':
                            self.notificar_servidores(payload['operation'], payload['data'], payload['old_data'])
                        elif payload['operation'] == 'DELETE':
                            self.notificar_servidores(payload['operation'], payload['data'])
        except OperationalError as e:
            self.stderr.write(self.style.ERROR(f"Error de base de datos: {e}"))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Ejecución interrumpida por el usuario."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error inesperado: {e}"))
        finally:
            # Cierre seguro de la conexión
            if connection.connection:
                try:
                    connection.connection.close()
                    self.stdout.write(self.style.SUCCESS("Conexión cerrada correctamente."))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error al cerrar la conexión: {e}"))

    def notificar_servidores(self, operacion, datos, antiguos_datos=None):
        if operacion == "INSERT":
            payload = {
                "operation": operacion,
                "data": datos
            }
        elif operacion == "UPDATE":
            payload = {
                "operation": operacion,
                "data": datos,
                "old_data": antiguos_datos
            }
        elif operacion == "DELETE":
            payload = {
                "operation": operacion,
                "data": datos
            }
        self.stderr.write(self.style.SUCCESS(payload))