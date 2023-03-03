from django.shortcuts import render
from .models import Producto
from django.urls import reverse_lazy, reverse 
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, ProductoForm
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from .serializer import ProductoSerializer

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
    success_url = reverse_lazy('producto_app:panel-producto')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)



class Panel(LoginRequiredMixin, TemplateView):
    template_name = "producto/panel.html"
    login_url = reverse_lazy ('producto_app:login-producto')
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'producto_app:login-producto'
            )
        )



class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "producto/lista.html"
    paginate_by = 5
    context_object_name = 'productos'
    ordering = 'identificador'

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


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "producto/create.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')

    



class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto/update.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de productos')
    login_url = reverse_lazy('producto_app:login-producto')

   



class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto/delete.html"
    success_url = reverse_lazy('producto_app:Lista de productos')



class ProductoListApiView(ListAPIView):

    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()
    
