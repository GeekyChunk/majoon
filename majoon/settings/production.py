from .base import *
import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ermia1303$majoondb',
        'USER': "ermia1303",
        'PASSWORD': 'majoon6969',
        'HOST': "ermia1303.mysql.pythonanywhere-services.com",
        'PORT': '3306',
    }
}


STATIC_ROOT = BASE_DIR / "static"

