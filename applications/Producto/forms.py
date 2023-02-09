from django import forms
from .models import Producto
from django.contrib.auth import authenticate 


class ProductoForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Producto
        fields = (
            'identificador',
            'descripcion',
            'precio',
            'marca',
            'proveedor',
        )


