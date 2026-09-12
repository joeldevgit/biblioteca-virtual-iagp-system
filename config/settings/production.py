from .base import *

import os
import dj_database_url


# =========================================================
# PRODUCCIÓN
# =========================================================

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]


# =========================================================
# HOSTS
# =========================================================

ALLOWED_HOSTS = [
    ".onrender.com",
]


# =========================================================
# BASE DE DATOS
# =========================================================

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ["DATABASE_URL"],
        conn_max_age=600,
        ssl_require=True,
    )
}


# =========================================================
# ARCHIVOS ESTÁTICOS
# =========================================================

STATIC_ROOT = BASE_DIR / "staticfiles"


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# =========================================================
# SEGURIDAD HTTPS
# =========================================================

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]