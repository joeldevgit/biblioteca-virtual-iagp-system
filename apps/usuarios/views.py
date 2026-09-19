from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from apps.usuarios.decorators import grupos_requeridos


# =========================================================
# GESTIÓN DE USUARIOS
# =========================================================

@login_required
@grupos_requeridos("Administrador")
def usuarios_lista(request):
    usuarios = User.objects.all().order_by("-id")

    return render(
        request,
        "usuarios/lista.html",
        {
            "usuarios": usuarios
        }
    )


@login_required
@grupos_requeridos("Administrador")
def usuario_crear(request):
    grupos = Group.objects.all().order_by("name")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        grupo_id = request.POST.get("grupo_id")

        usuario = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            email=email
        )

        if grupo_id:
            grupo = get_object_or_404(Group, id=grupo_id)
            usuario.groups.add(grupo)

        messages.success(
            request,
            "Usuario creado correctamente"
        )

        return redirect("usuarios:lista")

    return render(
        request,
        "usuarios/crear.html",
        {
            "grupos": grupos
        }
    )


@login_required
@grupos_requeridos("Administrador")
def usuario_editar(request, id):
    usuario = get_object_or_404(User, id=id)
    grupos = Group.objects.all().order_by("name")

    if request.method == "POST":
        usuario.first_name = request.POST.get("first_name")
        usuario.email = request.POST.get("email")

        grupo_id = request.POST.get("grupo_id")

        # Limpiar roles anteriores
        usuario.groups.clear()

        # Asignar nuevo rol
        if grupo_id:
            grupo = get_object_or_404(Group, id=grupo_id)
            usuario.groups.add(grupo)

        usuario.save()

        messages.success(
            request,
            "Usuario actualizado correctamente"
        )

        return redirect("usuarios:lista")

    grupo_actual = usuario.groups.first()

    return render(
        request,
        "usuarios/editar.html",
        {
            "usuario_obj": usuario,
            "grupos": grupos,
            "grupo_actual": grupo_actual,
        }
    )


@login_required
@grupos_requeridos("Administrador")
@require_POST
def usuario_estado(request, id):
    usuario = get_object_or_404(User, id=id)

    # Nunca permitir desactivar un superadministrador
    if not usuario.is_superuser:
        usuario.is_active = not usuario.is_active
        usuario.save()

        messages.success(
            request,
            "Estado del usuario actualizado"
        )

    return redirect("usuarios:lista")


# =========================================================
# AUTENTICACIÓN
# =========================================================

def login_view(request):

    # Si ya está autenticado, no necesita volver al login
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("usuarios:dashboard")

        messages.error(
            request,
            "Usuario o contraseña incorrectos"
        )

    return render(
        request,
        "usuarios/login.html"
    )


def logout_view(request):
    logout(request)

    return redirect("usuarios:login")



# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    if request.user.is_superuser:
        rol = "Superadministrador"

    elif request.user.groups.filter(name="Administrador").exists():
        rol = "Administrador"

    elif request.user.groups.filter(name="Bibliotecario").exists():
        rol = "Bibliotecario"

    elif request.user.groups.filter(name="Usuario").exists():
        rol = "Usuario"

    else:
        rol = "Sin rol"

    return render(
        request,
        "usuarios/dashboard.html",
        {
            "rol": rol,
        }
    )