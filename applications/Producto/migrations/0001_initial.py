# Generated by Django 3.2 on 2023-02-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('identificador', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion de Producto')),
                ('precio', models.IntegerField()),
                ('marca', models.CharField(max_length=50, verbose_name='marca de Producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
