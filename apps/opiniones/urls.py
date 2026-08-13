from django.urls import path
from . import views


app_name = "opiniones"


urlpatterns = [
    path("", views.opiniones, name="opiniones"),

    path("opiniones/", views.opiniones, name="opiniones"),
]
