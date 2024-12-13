from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Usamos SQLite en lugar de PostgreSQL
        'NAME': BASE_DIR / 'db.sqlite3',  # Ruta a la base de datos SQLite
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
