from django.urls import path
from . import views

app_name = "contactanos"

urlpatterns = [
    path("", views.index, name="index"),
]