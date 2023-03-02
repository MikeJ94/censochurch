# Generated by Django 3.2.13 on 2023-01-05 17:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'tblestado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Edad')),
                ('baptized', models.BooleanField(verbose_name='¿Es Bautizado?')),
                ('observationbap', models.CharField(max_length=200, verbose_name='Observacion de Bautismo')),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Hijo',
                'verbose_name_plural': 'Hijos',
                'db_table': 'tblhijo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ministerio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ministerio',
                'verbose_name_plural': 'Ministerios',
                'db_table': 'tblministerio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro')),
                ('name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=13, unique=True, verbose_name='# de Identidad')),
                ('date_birth', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de Nacimiento')),
                ('age', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('celular', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(blank=True, default='N/A', max_length=250, null=True, verbose_name='Direccion')),
                ('gender', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=10, verbose_name='Genero')),
                ('member', models.BooleanField(verbose_name='¿Es miembro?')),
                ('discipleship', models.BooleanField(verbose_name='¿Ha recibido Discipulado ICR?')),
                ('baptized', models.BooleanField(verbose_name='¿Es Bautizado?')),
                ('observationbap', models.CharField(blank=True, default='N/A', max_length=200, null=True, verbose_name='Observacion de Bautismo')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Foto')),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('childrenb', models.BooleanField(verbose_name='¿Tiene Hijos?')),
                ('familyrol', models.CharField(blank=True, choices=[('PAPÁ', 'PAPÁ'), ('MAMÁ', 'MAMÁ'), ('N/A', 'N/A')], default='N/A', max_length=10, null=True, verbose_name='Rol Familiar')),
                ('childrenmtm', models.ManyToManyField(blank=True, to='myapp.Hijo', verbose_name='Seleccione sus Hijos:')),
                ('ministry', models.ManyToManyField(to='myapp.Ministerio', verbose_name='Seleccione su Ministerio:')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'tblperson',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='hijo',
            name='ministry',
            field=models.ManyToManyField(blank=True, to='myapp.Ministerio', verbose_name='Seleccione su Ministerio:'),
        ),
    ]
