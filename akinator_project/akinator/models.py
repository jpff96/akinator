from django.db import models
import csv
# Create your models here.

class Users(models.Model):
    nombre_completo = models.CharField('Nombre completo', max_length=50)
    año = models.CharField('año nacimiento', max_length=50)
    sexo = models.CharField('sexo', max_length=50)
    color_pelo = models.CharField('color de pelo', max_length=50)
    altura = models.CharField('altura', max_length=50)
    deporte = models.CharField('deporte', max_length=50)
    vacaciones = models.CharField('vacaciones', max_length=50)
    instrumento = models.CharField('instrumento', max_length=50)
    int_montevideo = models.CharField('int/montevideo', max_length=50)
    departamento = models.CharField('departamento', max_length=50)
    profesion = models.CharField('profesion', max_length=50)
    materias_dadas = models.CharField('materias dadas', max_length=50)
    asesora = models.CharField('asesora', max_length=50)
    carrera = models.CharField('carrera', max_length=50)
    comienzo_carrera = models.CharField('comienzo carrera', max_length=50)
    asesor = models.CharField('asesor', max_length=50)
    secundaria = models.CharField('secundaria', max_length=50)
    fellow = models.CharField('fellow', max_length=50)
    ayudante = models.CharField('ayudante', max_length=50)
    como_vas = models.CharField('avance carrera', max_length=50)
