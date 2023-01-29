from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 


urlpatterns = [
    path(
        'inicial/',
        views.Inicio.as_view(),
        name ='Pagina Inicial'
    ),
] 