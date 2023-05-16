from .base import *
import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv("DB_NAME")),
        'USER': str(os.getenv("DB_USER")),
        'PASSWORD': str(os.getenv("DB_PASS")),
        'HOST': str(os.getenv("DB_HOST")),
        'PORT': str(os.getenv("DB_PORT")),
    }
}


STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = str(os.getenv("STATIC_URL"))

