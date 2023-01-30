from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'cliente_app'


urlpatterns = [

    path(
        'lista/',
        views.ClienteListView.as_view(),
        name='Lista de clientes'
    ),

    path(
        'buscar/',
        views.BuscarClienteListView.as_view(),
        name='Buscar cliente'
        ),

    path(
        'detalle/<pk>/',
        views.ClienteDetailView.as_view(),
        name='Detalle del cliente'
    ),


     path(
        'create/',
        views.ClienteCreateView.as_view(),
        name='Alta de clientes'
    ),

     path(
        'update/<pk>/',
        views.ClienteUpdateView.as_view(),
        name='Actualizar cliente'
    ),

     path(
        'delete/<pk>/',
        views.ClienteDeleteView.as_view(),
        name='Baja de cliente'
    ),


]

