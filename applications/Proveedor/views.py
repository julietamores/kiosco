from django.shortcuts import render
from .models import Proveedor

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
