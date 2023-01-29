from django.db import models

class Producto(models.Model):
    """Model definition for Producto."""

    descripcion = models.CharField('Descripcion de Producto', max_length=50)
    precio = models.IntegerField()

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return self.descripcion 

