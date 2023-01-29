from django.shortcuts import render
from .models import Home 

# Create your views here.

class Inicio(TemplateView):
    template_name = "inicio.html"
