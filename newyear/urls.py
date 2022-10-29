import imp
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("enn",views.Enn, name="enn")
]