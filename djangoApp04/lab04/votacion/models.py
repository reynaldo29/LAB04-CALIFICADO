from pyexpat import model
from django.db import models

# Create your models here.
class Region(models.Model):
    region = models.CharField(max_length=30)

class Candidato(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    nombre_candidato = models.CharField(max_length=40)
    apellido_candidato = models.CharField(max_length=40)
    profesion_candidato = models.CharField(max_length=30)