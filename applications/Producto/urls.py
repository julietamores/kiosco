from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'producto_app'


urlpatterns = [

    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-producto'
    ),
    path(
        'producto/panel/',
        views.Panel.as_view(),
        name='panel-producto'
    ),
    path(
        'producto/logout/',
        views.LogoutView.as_view(),
        name='logout-producto'
    ),

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

