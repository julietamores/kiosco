# Generated by Django 3.2 on 2023-02-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('identificador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre del proveedor')),
                ('email', models.CharField(max_length=50, verbose_name='email del proveedor')),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]