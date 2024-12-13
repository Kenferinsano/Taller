from rest_framework import serializers
from .models import alumnos, calificacion

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = calificacion
        fields = ['id', 'valor']

class AlumnoSerializer(serializers.ModelSerializer):
    notas = CalificacionSerializer(many=True, read_only=True)

    class Meta:
        model = alumnos
        fields = ['id', 'nombre', 'edad', 'correo', 'estado_activo', 'notas']