from django.shortcuts import render
from .models import Proveedor
from django.urls import reverse_lazy, reverse 
from .forms import ProveedorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, ProveedorForm
from rest_framework.generics import ListAPIView
from .serializer import ProveedorSerializer
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
    success_url = reverse_lazy('proveedor_app:panel-proveedor')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(LoginRequiredMixin, TemplateView):
    template_name = "proveedor/panel.html"
    login_url = reverse_lazy ('proveedor_app:login-proveedor')

    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'proveedor_app:login-proveedor'
            )
        )



class ProveedorListView(LoginRequiredMixin, ListView):
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


class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de proveedores')
    login_url = reverse_lazy('proveedor_app:login-proveedor')

   



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


class ProveedorListApiView(ListAPIView):

    serializer_class = ProveedorSerializer

    def get_queryset(self):
        return Proveedor.objects.all()
