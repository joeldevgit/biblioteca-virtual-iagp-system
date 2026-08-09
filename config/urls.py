from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),


    path("", include("apps.home.urls")),

    path("nosotros/", include("apps.nosotros.urls")),
    path("catalogo-academico/", include("apps.catalogo_academico.urls")),
    path("blog/", include("apps.blog.urls")),
    path("contactanos/", include("apps.contactanos.urls")),
    path("preinscripcion/", include("apps.preinscripcion.urls")),

    path("biblioteca/", include("apps.biblioteca.urls")),
    path("opiniones-osce/", include("apps.opiniones_osce.urls")),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



if settings.DEBUG and "django_browser_reload" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]