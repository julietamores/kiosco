from django.shortcuts import render
from .models import Proveedor
from django.urls import reverse_lazy, reverse 
from .forms import ProveedorForm

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


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/lista.html"
    paginate_by = 8
    context_object_name = 'proveedores'

    def get_queryset(self):
        lista = Proveedor.objects.all()
        return lista

    


class BuscarProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/buscar.html"
    ordering = 'nombre'
    context_object_name = 'proveedores'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Proveedor.objects.filter(
            nombre__icontains = palabra_clave
        )
        return lista 

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor/detalle.html"
    context_object_name = 'detalle'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de proveedores')

    def form_valid(self, form):
        prov = form.save(commit=False)
        prov.identificador = prov.nombre + '' + prov.telefono 
        prov.save()
        return super(ProveedorCreateView,self).form_valid(form)



class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor/update.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de proveedores')

    def form_valid(self, form):
        prov = form.save(commit=False)
        prov.identificador = prov.nombre + '' + prov.telefono
        prov.save()
        return super(ProveedorUpdateView,self).form_valid(form)



class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedor/delete.html"
    success_url = reverse_lazy('proveedor_app:Lista de proveedores')



