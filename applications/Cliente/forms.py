from django import forms
from .models import Cliente 
from django.contrib.auth import authenticate 


class ClienteForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Cliente
        fields = (
            'apellido',
            'nombre',
            'razonSocial',
            'documento',
        )


