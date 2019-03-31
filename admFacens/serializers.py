from rest_framework import serializers
from .models import *

class ObjetivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objetivo
        fields = '__all__'

class CompetenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competencia
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        depth = 1
        fields = '__all__'

class CursoObjetivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CursoObjetivo
        depth = 1
        fields = '__all__'