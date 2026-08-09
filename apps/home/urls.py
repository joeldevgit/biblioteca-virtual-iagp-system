from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),


    path("normatividad-y-directivas/", views.normatividad_directiva, name="normatividad_directiva"),
]