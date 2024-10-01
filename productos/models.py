from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False) 
    unidades = models.IntegerField(blank=True, null=False)