from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length = 250)
    edad = models.IntegerField()
    estaVacunado = models.BooleanField(default = False)