from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-ixyp)xg_n5*z*i)$-i%4%_2z-s9&-ae6ffisc-jdory-m9$-^&"

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    "django_browser_reload",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


