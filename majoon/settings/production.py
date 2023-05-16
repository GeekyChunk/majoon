from .base import *
import os

DEBUG = False

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


STATIC_ROOT = "/home/ermia1303/app/static"
STATIC_URL = "static/"

ALLOWED_HOSTS = ["*"]