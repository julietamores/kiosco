from django.shortcuts import render
from .models import Cliente
from django.urls import reverse_lazy, reverse 
from .forms import ClienteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, ClienteForm
from rest_framework.generics import ListAPIView
from .serializer import ClienteSerializer
from django.views.generic.edit import (
    FormView
)

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


class LoginUser(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('cliente_app:panel-cliente') 
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(LoginRequiredMixin, TemplateView):
    template_name = "cliente/panel.html"
    login_url = reverse_lazy ('cliente_app:login-cliente')
    

    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'cliente_app:login-cliente'
            )
        )





class ClienteListView(LoginRequiredMixin ,ListView):
    model = Cliente
    template_name = "cliente/lista.html"
    paginate_by = 8
    context_object_name = 'clientes'

    def get_queryset(self):
        lista = Cliente.objects.all()
        return lista

    


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


class ClienteCreateView(LoginRequiredMixin, CreateView):
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


class ClienteListApiView(ListAPIView):

    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()