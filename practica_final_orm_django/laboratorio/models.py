from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default="")
    pais = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Laboratorios"

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director_general')
    especialidad = models.CharField(max_length=100,default="")

    def __str__(self):
        return f"{self.nombre} - Director de {self.laboratorio.nombre}"

    class Meta:
        verbose_name = "Director general"
        verbose_name_plural = "Director generales"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    f_fabricacion = models.DateField(validators=[MinValueValidator(limit_value=date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"

    class Meta:
        verbose_name_plural = "Productos"