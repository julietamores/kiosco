# Generated by Django 3.2 on 2023-01-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=50, verbose_name='Descripcion de Producto'),
        ),
    ]