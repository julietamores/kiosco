from django import forms
from .models import Proveedor
from django.contrib.auth import authenticate 


class ProveedorForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Proveedor
        fields = (
            'identificador',
            'nombre',
            'email',
            'telefono',
        )


