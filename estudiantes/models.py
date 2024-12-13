from django.db import models

# Create your models here.

class alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    estado_activo = models.BooleanField(default=True)
    
class calificacion(models.Model):
    estudiante = models.ForeignKey(alumnos, related_name='notas', on_delete=models.CASCADE)
    valor = models.FloatField()
    
def __str__(self):
    return self.nombre

def __str__(self):
    return self.edad

def __str__(self):
    return self.correo

def __str__(self):
    return self.estado_activo