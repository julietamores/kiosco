from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'producto_app'


urlpatterns = [

    path(
        'producto/lista/',
        views.ProductoListView.as_view(),
        name='Lista de productos'
    ),

    path(
        'producto/buscar/',
        views.BuscarProductoListView.as_view(),
        name='Buscar producto'
        ),

    path(
        'producto/detalle/<pk>/',
        views.ProductoDetailView.as_view(),
        name='Detalle del producto'
    ),


     path(
        'producto/create/',
        views.ProductoCreateView.as_view(),
        name='Alta de producto'
    ),

     path(
        'producto/update/<pk>/',
        views.ProductoUpdateView.as_view(),
        name='Actualizar producto'
    ),

     path(
        'producto/delete/<pk>/',
        views.ProductoDeleteView.as_view(),
        name='Eliminar Producto'
    ),


]

