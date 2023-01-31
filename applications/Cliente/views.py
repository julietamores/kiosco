from django.shortcuts import render
from .models import Cliente
from django.urls import reverse_lazy, reverse 
from .forms import ClienteForm

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
    paginate_by = 3
    context_object_name = 'cliente'


class BuscarClienteListView(ListView):
    model = Cliente
    template_name = "cliente/buscar.html"
    ordering = 'apellidos'
    context_object_name = 'clientes'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Cliente.objects.filter(
            apellido__icontains = palabra_clave
        )
        return lista 

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/detalle.html"
    context_object_name = 'detalle'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cliente/create.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de clientes')

    def form_valid(self, form):
        clientela = form.save(commit=False)
        clientela.razonSocial = clientela.nombre + '' + clientela.apellido 
        clientela.save()
        return super(ClienteCreateView,self).form_valid(form)



class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cliente/update.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de clientes')

    def form_valid(self, form):
        clientela = form.save(commit=False)
        clientela.razonSocial = clientela.nombre + '' + clientela.apellido
        clientela.save()
        return super(ClienteUpdateView,self).form_valid(form)



class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente/delete.html"
    success_url = reverse_lazy('cliente_app:Lista de clientes')



