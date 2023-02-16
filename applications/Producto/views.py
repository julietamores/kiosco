from django.shortcuts import render
from .models import Producto
from django.urls import reverse_lazy, reverse 
from .forms import ProductoForm

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


class ProductoListView(ListView):
    model = Producto
    template_name = "producto/lista.html"
    paginate_by = 8
    context_object_name = 'productos'

    def get_queryset(self):
        lista = Producto.objects.all()
        return lista

    

class BuscarProductoListView(ListView):
    model = Producto
    template_name = "producto/buscar.html"
    ordering = 'identificador'
    context_object_name = 'producto'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Producto.objects.filter(
            identificador__icontains = palabra_clave
        )
        return lista 

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/detalle.html"
    context_object_name = 'detalle'


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto/create.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')

    def form_valid(self, form):
        prod = form.save(commit=False)
        prod.identificador = prod.descripcion + '' + prod.item.marca
        prod.save()
        return super(ProductoCreateView,self).form_valid(form)



class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto/update.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')

    def form_valid(self, form):
        prod = form.save(commit=False)
        prod.identificador = prod.descripcion + '' + prod.item.marca
        prod.save()
        return super(ProductoUpdateView,self).form_valid(form)



class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto/delete.html"
    success_url = reverse_lazy('producto_app:Lista de productos')
