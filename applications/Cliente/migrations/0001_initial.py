# Generated by Django 3.2 on 2023-02-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=50, verbose_name='nombre del cliente')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido del cliente')),
                ('razonSocial', models.CharField(max_length=50, verbose_name='razonSocial del cliente')),
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='cliente', verbose_name='imagen')),
                ('telefono', models.IntegerField(default=0, verbose_name='telefono del cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
