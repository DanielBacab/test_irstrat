from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    lugar_origen = models.CharField(max_length=100)