from django.db import models
# Create your models here.
class Usuarios(models.Model):
    nombre=models.CharField(max_length=15)
    Telefono=models.CharField(max_length=15)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField(max_length=254)