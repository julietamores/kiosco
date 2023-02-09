from django.db import models

# Create your models here.

class Cliente(models.Model):
    """Model definition for Cliente."""

    nombre = models.CharField('nombre del cliente', max_length=50)
    apellido = models.CharField('apellido del cliente', max_length=50)
    razonSocial = models.CharField('razonSocial del cliente', max_length=50)
    documento = models.IntegerField(primary_key=True)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.razonSocial

