from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import alumnos, calificacion
from .serializers import AlumnoSerializer, CalificacionSerializer
from django.shortcuts import render

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = alumnos.objects.all()
    serializer_class = AlumnoSerializer

    @action(detail=True, methods=['post'])
    def añadir_nota(self, request, pk=None):
        estudiante = self.get_object()
        nota = request.data.get('valor')
        if nota:
            calificacion.objects.create(estudiante=estudiante, valor=float(nota))
            return Response({'message': 'Nota agregada correctamente'})
        return Response({'error': 'Debe enviar una nota'}, status=400)

    @action(detail=True, methods=['get'])
    def aprobacion(self, request, pk=None):
        estudiante = self.get_object()
        notas = estudiante.notas.all()
        promedio = sum(n.valor for n in notas) / len(notas) if notas else 0
        aprobado = promedio >= 3.0
        return Response({'promedio': promedio, 'aprobado': aprobado})