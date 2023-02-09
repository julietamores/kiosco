from django.db import models
from applications.Proveedor.models import Proveedor




# Create your models here.
class Marca(models.Model):
    """Model definition for Marca."""

    marca = models.CharField("Marca", max_length=50)
    
    class Meta:
        """Meta definition for Marca."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marca."""
        return self.marca


class Producto(models.Model):
    """Model definition for Producto."""

    identificador = models.IntegerField( primary_key=True)
    descripcion = models.CharField('Descripcion de Producto', max_length=50)
    precio = models.IntegerField()
    marca = models.ManyToManyField(Marca)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default='')

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return f"{self.identificador} {self.nombre}"



    
  
   
