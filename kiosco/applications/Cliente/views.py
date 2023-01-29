from django.shortcuts import render
from .models import Cliente

# Create your views here.
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/lista.html"
    ordering = 'apellidos'
    context_object_name = 'cliente'
