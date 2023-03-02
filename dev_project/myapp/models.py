from django.db import models
from datetime import datetime
import os
from django.forms import model_to_dict
from dev_project.settings import MEDIA_URL, STATIC_URL


def filepath(request, filename):
    old_filename = filename
    #timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    timeNow = datetime.datetime.now('%Y-%m-%d')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('avatar/', filename)

class Ministerio(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name # Muestra como se vera el Listado en el Panel de Administracion
    
    class Meta:
        verbose_name = 'Ministerio' # Da el Nombre en el Panel de Administracion
        verbose_name_plural = 'Ministerios' # Da el Nombre en el Panel de Administracion
        db_table = 'tblministerio'
        ordering = ['id']

class Estado(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name # Muestra como se vera el Listado en el Panel de Administracion
    
    class Meta:
        verbose_name = 'Estado' # Da el Nombre en el Panel de Administracion
        verbose_name_plural = 'Estados' # Da el Nombre en el Panel de Administracion
        db_table = 'tblestado'
        ordering = ['id']

class Hijo(models.Model):
    name = models.CharField(max_length=50,unique=True)
    age = models.PositiveIntegerField(default=0,verbose_name='Edad') # Para que no acepte Enteros Negati
    baptized = models.BooleanField(verbose_name='¿Es Bautizado?')
    observationbap = models.CharField(default='N/A',max_length=200, verbose_name='Observacion de Bautismo',blank=True)
    ministry = models.ManyToManyField(Ministerio, verbose_name='Seleccione su Ministerio:')
    date_updated = models.DateTimeField(auto_now = True) # Fecha y Hora / Se ira modificando


    def __str__(self):
        return self.name # Muestra como se vera el Listado en el Panel de Administracion

    def toJSON(self):
        item = model_to_dict(self)
        item['ministry'] = [model_to_dict(t) for t in self.ministry.all()]
        return item
    
    class Meta:
        verbose_name = 'Hijo' # Da el Nombre en el Panel de Administracion
        verbose_name_plural = 'Hijos' # Da el Nombre en el Panel de Administracion
        db_table = 'tblhijo'
        ordering = ['id']

# Create your models here.
class Person(models.Model):
    date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de Registro') # Fecha
    name = models.CharField(max_length=50, verbose_name='Nombres')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    dni = models.CharField(max_length=13,unique=True,verbose_name='# de Identidad') 
    date_birth = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento',null=True,blank=True) # Fecha
    age = models.PositiveIntegerField(default=0,verbose_name='Edad',null=True,blank=True) # Para que no acepte Enteros Negativos
    celular = models.PositiveIntegerField(default=0,null=True,blank=True)
    address = models.CharField(default='N/A',max_length=250, verbose_name='Direccion',null=True,blank=True)
    #----------------------------------------------------------------#
    MASCULINO = 'MASCULINO'
    FEMENINO = 'FEMENINO'
    GENDER_IN_CHOICES = [
        (MASCULINO, 'MASCULINO'),
        (FEMENINO, 'FEMENINO'),
    ]
    gender = models.CharField(max_length=10,choices=GENDER_IN_CHOICES,verbose_name='Genero')
    #----------------------------------------------------------------#
    member = models.BooleanField(verbose_name='¿Es miembro?')
    discipleship = models.BooleanField(verbose_name='¿Ha recibido Discipulado ICR?')
    baptized = models.BooleanField(verbose_name='¿Es Bautizado?')
    observationbap = models.CharField(default='N/A',max_length=200, verbose_name='Observacion de Bautismo',null=True,blank=True)
    ministry = models.ManyToManyField(Ministerio,verbose_name='Seleccione su Ministerio:')
    state = models.ForeignKey(Estado, verbose_name='Estado', null=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/',verbose_name='Foto',max_length=100)
    date_updated = models.DateTimeField(auto_now = True) # Fecha y Hora / Se ira modificando
    childrenb = models.BooleanField(verbose_name='¿Tiene Hijos?')
     #----------------------------------------------------------------#
    PAPA = 'PAPÁ'
    MAMA = 'MAMÁ'
    N_A = 'N/A'
    GENDER_IN_CHOICES = [
        (PAPA, 'PAPÁ'),
        (MAMA, 'MAMÁ'),
        (N_A, 'N/A'),
    ]
    familyrol = models.CharField(default='N/A',max_length=10,choices=GENDER_IN_CHOICES,verbose_name='Rol Familiar',null=True,blank=True)
    #----------------------------------------------------------------#
    childrenmtm = models.ManyToManyField(Hijo,verbose_name='Seleccione sus Hijos:',blank=True)
    
    #Agregando Propiedades a la Entidad
    def __str__(self):
        texto = " {0} ({1})"
        return texto.format(self.name, self.lastname) # Muestra como se vera el Listado en el Panel de Administracion

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/avatar.png')

    class Meta:
        verbose_name = 'Persona' # Da el Nombre en el Panel de Administracion
        verbose_name_plural = 'Personas' # Da el Nombre en el Panel de Administracion
        db_table = 'tblperson'
        ordering = ['id']


