from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'cliente_app'


urlpatterns = [

    path(
        'cliente/lista/',
        views.ClienteListView.as_view(),
        name='Lista de clientes'
    ),

    path(
        'cliente/buscar/',
        views.BuscarClienteListView.as_view(),
        name='Buscar cliente'
        ),

    path(
        'cliente/detalle/<pk>/',
        views.ClienteDetailView.as_view(),
        name='Detalle del cliente'
    ),


     path(
        'cliente/create/',
        views.ClienteCreateView.as_view(),
        name='Alta de clientes'
    ),

     path(
        'cliente/update/<pk>/',
        views.ClienteUpdateView.as_view(),
        name='Actualizar cliente'
    ),

     path(
        'cliente/delete/<pk>/',
        views.ClienteDeleteView.as_view(),
        name='Baja de cliente'
    ),


]

