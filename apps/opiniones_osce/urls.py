from django.urls import path
from . import views


app_name = "opiniones_osce"


urlpatterns = [
    path("", views.opiniones, name="opiniones"),
]
