from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'proveedor_app'


urlpatterns = [

    path(
        'lista/',
        views.ProveedorListView.as_view(),
        name='Lista de proveedores'
    ),

    path(
        'buscar/',
        views.BuscarProveedorListView.as_view(),
        name='Buscar proveedor'
        ),

    path(
        'detalle/<pk>/',
        views.ProveedorDetailView.as_view(),
        name='Detalle del proveedor'
    ),


     path(
        'create/',
        views.ProveedorCreateView.as_view(),
        name='Alta de proveedores'
    ),

     path(
        'update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Actualizar proveedor'
    ),

     path(
        'delete/<pk>/',
        views.ProveedorDeleteView.as_view(),
        name='Baja de proveedor'
    ),


]

