from django.contrib import admin
from django.urls import path, re_path, include 
from . import views 

app_name = 'cliente_app'

urlpatterns = [

    path(
        'lista/',
        views.EmpleadoListView.as_view(),
        name='Lista de clientes'
    ),



