from django.contrib import admin
from .models import Cliente 

admin.site.register(Cliente, ClienteAdmin )

class ClienteAdmin (admin.ModelAdmin): 
    list_display = (
        'apellido',
        'nombre',
        'razonSocial',
        'documento',
    )

    search_fields = ('apellidos',)
    list_filter = ('razonSocial',)
