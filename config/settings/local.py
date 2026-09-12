from .base import *


# =========================================================
# DESARROLLO LOCAL
# =========================================================

DEBUG = True

SECRET_KEY = "django-insecure-ixyp)xg_n5*z*i)$-i%4%_2z-s9&-ae6ffisc-jdory-m9$-^&"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]


# =========================================================
# BASE DE DATOS LOCAL
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "biblioteca_iagp",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}