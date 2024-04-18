from django.db import models


class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)  
    email = models.EmailField(max_length=75)  
    fechaNacimiento = models.DateField()  
    pago = models.PositiveSmallIntegerField()
