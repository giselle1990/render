from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_gestion = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cuil = models.CharField(max_length=11, default='12345678')
    telefono = models.CharField(max_length=20, default='0000000000')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f'Datos de {self.nombre} {self.apellido}'

class RegistroHistorial(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cuil = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
