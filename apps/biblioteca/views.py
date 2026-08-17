from django.shortcuts import get_object_or_404, render

from .models import (
    Categoria,
    Documento,
    Institucion,
    TipoDocumento,
)

from django.core.paginator import Paginator
from django.db.models import Q


def biblioteca(request):

    categorias = Categoria.objects.filter(
        activo=True
    )

    categoria_slug = request.GET.get("categoria")

    categoria_activa = None

    if categoria_slug:
        categoria_activa = get_object_or_404(
            categorias,
            slug=categoria_slug
        )
    else:
        categoria_activa = categorias.first()

    documentos = (
        Documento.objects
        .filter(
            activo=True,
            categoria=categoria_activa
        )
        .select_related(
            "categoria",
            "institucion",
            "tipo",
        )
    )

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

    tipos = (
        TipoDocumento.objects
        .filter(
            activo=True,
            categoria=categoria_activa,
        )
        .order_by("nombre")
    )

    return render(
        request,
        "biblioteca/biblioteca.html",
        {
            "categorias": categorias,
            "categoria_activa": categoria_activa,
            "documentos": documentos,
            "instituciones": instituciones,
            "tipos": tipos,
        }
    )



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

    # IMPORTANTE:
    # El tipo SÍ puede afectar los años disponibles.
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
    # RESPUESTA AJAX
    # =====================================================
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

        return render(
            request,
            "biblioteca/_resultados.html",
            {
                "documentos": documentos,
                "total_documentos": total_documentos,
            }
        )

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
    # CONTEXTO
    # =====================================================
    context = {

        "documentos": documentos,

        "total_documentos": total_documentos,

        "categorias": categorias,

        "instituciones": instituciones,

        "tipos": tipos,

        "anios": anios,

        # -----------------------------------------------
        # CONTEXTO ACTUAL
        # -----------------------------------------------

        "categoria_seleccionada": categoria_slug,

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