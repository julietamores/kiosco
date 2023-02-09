from django.db import models

class Proveedor(models.Model):
    """Model definition for Proveedor."""

    identificador = models.IntegerField(primary_key=True)
    nombre = models.CharField('nombre del proveedor', max_length=50)
    email = models.CharField('email del proveedor', max_length=50)
    telefono = models.IntegerField()

    class Meta:
        """Meta definition for Proveedor."""

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        """Unicode representation of Proveedor."""
        return self.nombre 

