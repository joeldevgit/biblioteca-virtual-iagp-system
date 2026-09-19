from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def grupos_requeridos(*nombres_grupos):
    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            # Superadministrador: acceso total
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # Verificar grupos permitidos
            if request.user.groups.filter(
                name__in=nombres_grupos
            ).exists():
                return view_func(request, *args, **kwargs)

            # Sin permisos
            messages.error(
                request,
                "No tienes permiso para acceder a esta sección."
            )

            return redirect("/")

        return wrapper

    return decorator