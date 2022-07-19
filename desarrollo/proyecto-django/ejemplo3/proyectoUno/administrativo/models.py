from django.db import models

# Create your models here.

class Propietario(models.Model):
    nacionalidad_tipo = (
    ('ecuatoriana','Ecuatoriana'),
    ('peruana','Peruana'),
    ('colombiana','Colombiana'),

    )
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30,  \
            choices= nacionalidad_tipo)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)
    

class Departamento(models.Model):
    costo_depar = models.CharField(max_length=100)
    num_cuartos = models.CharField(max_length=100)
    num_baños = models.CharField(max_length=100)
    valor_alicuota = models.CharField(max_length=100)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %s %s" % (self.costo_depar,
         self.num_cuartos,
         self.num_baños,
         self.valor_alicuota)

