from django.shortcuts import get_object_or_404, render, redirect
from django.http import FileResponse, Http404

from .models import (
    Categoria,
    Documento,
    Institucion,
    TipoDocumento,
)

from django.core.paginator import Paginator
from django.db.models import Q


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import DocumentoForm
from apps.usuarios.decorators import grupos_requeridos



@login_required
def biblioteca(request):

    # =====================================================
    # CATEGORÍAS
    # =====================================================
    categorias = ( 
        Categoria.objects 
        .filter(activo=True) 
        .order_by("nombre") 
    )

    categoria_slug = request.GET.get("categoria")

    if categoria_slug:

        categoria_activa = get_object_or_404(
            categorias,
            slug=categoria_slug
        )

    else:

        categoria_activa = categorias.first()


    # =====================================================
    # DATOS DE LA CATEGORÍA ACTIVA
    # =====================================================

    tipos = TipoDocumento.objects.none()
    documentos = Documento.objects.none()
    instituciones = Institucion.objects.none()


    if categoria_activa:

        # =================================================
        # TIPOS DE DOCUMENTO
        # =================================================

        tipos = (
            TipoDocumento.objects
            .filter(
                activo=True,
                categoria=categoria_activa,
            )
            .order_by("nombre")
        )



   
        # =================================================
        # INSTITUCIONES
        # =================================================

        instituciones = (
            Institucion.objects
            .filter(
                activo=True,
                documentos__categoria=categoria_activa,
                documentos__activo=True,
            )
            .distinct()
            .order_by("nombre")
        )


    # =====================================================
    # CONTEXTO
    # =====================================================

    context = {

        "categorias": categorias,

        "categoria_activa":
            categoria_activa,

        "instituciones":
            instituciones,

        "tipos":
            tipos,

    }


    return render(
        request,
        "biblioteca/biblioteca.html",
        context
    )






@login_required
def listado_documentos(request):

    # =====================================================
    # PARÁMETROS
    # =====================================================

    categoria_slug = request.GET.get("categoria", "").strip()
    institucion_id = request.GET.get("institucion", "").strip()
    tipo_id = request.GET.get("tipo", "").strip()
    anio = request.GET.get("anio", "").strip()
    buscar = request.GET.get("buscar", "").strip()


    # =====================================================
    # TIPO POR DEFECTO: OPINIONES
    # =====================================================

    if not tipo_id:

        tipos_opiniones = (
            TipoDocumento.objects
            .filter(
                activo=True,
                documentos__activo=True,
                documentos__categoria__slug=categoria_slug,
                documentos__institucion_id=institucion_id,
            )
            .filter(
                Q(nombre__iexact="Opiniones") |
                Q(nombre__iexact="Opinión")
            )
            .distinct()
            .order_by("id")
        )

        tipo_opiniones = tipos_opiniones.first()

        if tipo_opiniones:
            tipo_id = str(tipo_opiniones.id)

    # =====================================================
    # DOCUMENTOS BASE
    # =====================================================

    documentos = (
        Documento.objects
        .filter(activo=True)
        .select_related(
            "categoria",
            "institucion",
            "tipo",
        )
    )


    # =====================================================
    # CATEGORÍA
    # =====================================================

    if categoria_slug:

        documentos = documentos.filter(
            categoria__slug=categoria_slug
        )


    # =====================================================
    # INSTITUCIÓN
    # =====================================================

    if institucion_id:

        documentos = documentos.filter(
            institucion_id=institucion_id
        )


    # =====================================================
    # TIPO
    # =====================================================

    if tipo_id:

        documentos = documentos.filter(
            tipo_id=tipo_id
        )


    # =====================================================
    # AÑO
    # =====================================================

    if anio:

        documentos = documentos.filter(
            anio=anio
        )


    # =====================================================
    # BÚSQUEDA
    # =====================================================

    if buscar:

        documentos = documentos.filter(
            Q(titulo__icontains=buscar)
            | Q(tema__icontains=buscar)
        )


    # =====================================================
    # TOTAL DE DOCUMENTOS FILTRADOS
    # =====================================================

    total_documentos = documentos.count()


    # =====================================================
    # CATEGORÍAS
    # =====================================================
    categorias = (
        Categoria.objects
        .filter(activo=True)
        .order_by("nombre")
    )


    # =====================================================
    # INSTITUCIONES DISPONIBLES
    # DEPENDEN DE LA CATEGORÍA
    # =====================================================

    instituciones = (
        Institucion.objects
        .filter(
            activo=True,
            documentos__activo=True,
        )
    )

    if categoria_slug:

        instituciones = instituciones.filter(
            documentos__categoria__slug=categoria_slug
        )

    instituciones = (
        instituciones
        .distinct()
        .order_by("nombre")
    )


    # =====================================================
    # TIPOS DISPONIBLES
    # DEPENDEN DE CATEGORÍA + INSTITUCIÓN
    # =====================================================

    tipos = (
        TipoDocumento.objects
        .filter(
            activo=True,
            documentos__activo=True,
        )
    )

    if categoria_slug:

        tipos = tipos.filter(
            documentos__categoria__slug=categoria_slug
        )

    if institucion_id:

        tipos = tipos.filter(
            documentos__institucion_id=institucion_id
        )

    tipos = (
        tipos
        .distinct()
        .order_by("nombre")
    )


    # =====================================================
    # AÑOS DISPONIBLES
    # DEPENDEN DE CATEGORÍA + INSTITUCIÓN + TIPO
    # =====================================================

    documentos_para_anios = (
        Documento.objects
        .filter(activo=True)
    )

    if categoria_slug:

        documentos_para_anios = documentos_para_anios.filter(
            categoria__slug=categoria_slug
        )

    if institucion_id:

        documentos_para_anios = documentos_para_anios.filter(
            institucion_id=institucion_id
        )

    # El tipo seleccionado también afecta los años
    if tipo_id:

        documentos_para_anios = documentos_para_anios.filter(
            tipo_id=tipo_id
        )

    anios = (
        documentos_para_anios
        .filter(anio__isnull=False)
        .values_list("anio", flat=True)
        .distinct()
        .order_by("-anio")
    )


    # =====================================================
    # PAGINACIÓN
    # =====================================================

    paginator = Paginator(documentos, 10)

    pagina = request.GET.get("page")

    documentos = paginator.get_page(pagina)


    # =====================================================
    # VALORES SELECCIONADOS
    # =====================================================

    try:

        institucion_seleccionada = (
            int(institucion_id)
            if institucion_id
            else None
        )

    except ValueError:

        institucion_seleccionada = None


    try:

        tipo_seleccionado = (
            int(tipo_id)
            if tipo_id
            else None
        )

    except ValueError:

        tipo_seleccionado = None


    try:

        anio_seleccionado = (
            int(anio)
            if anio
            else None
        )

    except ValueError:

        anio_seleccionado = None


    # =====================================================
    # RESPUESTA AJAX
    # =====================================================

    if request.headers.get(
        "X-Requested-With"
    ) == "XMLHttpRequest":

        return render(
            request,
            "biblioteca/_resultados.html",
            {
                "documentos": documentos,
                "total_documentos": total_documentos,
            }
        )


    # =====================================================
    # CONTEXTO
    # =====================================================
    # =====================================================
    # TIPO ACTUALMENTE SELECCIONADO (para el título dinámico)
    # =====================================================

    tipo_actual = None

    if tipo_seleccionado:

        tipo_actual = next(
            (t for t in tipos if t.id == tipo_seleccionado),
            None,
        )

    context = {

        "tipo_actual": tipo_actual,

        "documentos": documentos,

        "total_documentos": total_documentos,

        "categorias": categorias,

        "instituciones": instituciones,

        "tipos": tipos,

        "anios": anios,

        "categoria_seleccionada":
            categoria_slug,

        "institucion_seleccionada":
            institucion_seleccionada,

        "tipo_seleccionado":
            tipo_seleccionado,

        "anio_seleccionado":
            anio_seleccionado,

        "buscar_seleccionado":
            buscar,
    }


    return render(
        request,
        "biblioteca/listado.html",
        context
    )





@login_required
def detalle_documento(request, pk):

    documento = get_object_or_404(
        Documento.objects.select_related(
            "categoria",
            "institucion",
            "tipo",
        ),
        pk=pk,
        activo=True,
    )

    return render(
        request,
        "biblioteca/detalle.html",
        {
            "documento": documento,
        }
    )






# =========================================================
# DESCARGA DE DOCUMENTOS (requiere estar logueado)
# =========================================================

@login_required
def documento_descargar(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk,
        activo=True,
    )

    # Archivo subido directamente al servidor
    if documento.pdf:
        modo_ver = request.GET.get("modo") == "ver"

        return FileResponse(
            documento.pdf.open("rb"),
            as_attachment=not modo_ver,
            filename=documento.pdf.name.split("/")[-1],
        )

    # Documento alojado externamente (enlace)
    if documento.pdf_url:
        return redirect(documento.pdf_url)

    raise Http404("Este documento no tiene un archivo disponible.")






# =========================================================
# GESTIÓN DE DOCUMENTOS
# =========================================================

@login_required
@grupos_requeridos("Administrador", "Bibliotecario")
def documento_crear(request):

    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Documento creado correctamente."
            )

            return redirect("biblioteca:gestion_documentos")

    else:
        form = DocumentoForm()

    return render(
        request,
        "biblioteca/gestion/documento_form.html",
        {
            "form": form,
            "titulo": "Nuevo documento",
        }
    )


@login_required
@grupos_requeridos("Administrador", "Bibliotecario")
def documento_editar(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk
    )

    if request.method == "POST":
        form = DocumentoForm(
            request.POST,
            request.FILES,
            instance=documento
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Documento actualizado correctamente."
            )

            return redirect(
                "biblioteca:gestion_documentos"
            )

    else:
        form = DocumentoForm(
            instance=documento
        )

    return render(
        request,
        "biblioteca/gestion/documento_form.html",
        {
            "form": form,
            "titulo": "Editar documento",
            "documento": documento,
        }
    )


@login_required
@grupos_requeridos("Administrador", "Bibliotecario")
@require_POST
def documento_estado(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk
    )

    documento.activo = not documento.activo
    documento.save()

    messages.success(
        request,
        "Estado del documento actualizado."
    )

    return redirect(
        "biblioteca:gestion_documentos"
    )


@login_required
@grupos_requeridos("Administrador", "Bibliotecario")
def gestion_documentos(request):

    documentos = (
        Documento.objects
        .select_related(
            "categoria",
            "institucion",
            "tipo",
        )
        .order_by(
            "-activo",
            "-anio",
            "-fecha",
            "-id",
        )
    )

    return render(
        request,
        "biblioteca/gestion/documentos.html",
        {
            "documentos": documentos,
        }
    )