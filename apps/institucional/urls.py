from django.urls import path
from . import views

app_name = "institucional"

urlpatterns = [
    path("quienes-somos/", views.quienes_somos, name="quienes_somos"),
    path("mision-vision/", views.mision_vision, name="mision_vision"),
    path("estructura/", views.estructura, name="estructura"),
]