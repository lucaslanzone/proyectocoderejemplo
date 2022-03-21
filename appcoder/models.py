from django.db import models
from django.forms import CharField

# Create your models here.
class Curso(models.Model):

    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(primary_key=True)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_entregado = models.DateField()
    entregado = models.BooleanField()
