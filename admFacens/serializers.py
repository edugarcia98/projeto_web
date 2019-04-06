from rest_framework import serializers
from .models import *

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        depth = 1
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        depth = 1
        fields = '__all__'

class ObjetivoSerializer(serializers.ModelSerializer):

    curso = CursoSerializer(read_only=True)

    curso_id = serializers.PrimaryKeyRelatedField(
       queryset=Curso.objects.all(), source='curso', write_only=True
    )

    class Meta:
        model = Objetivo
        fields = '__all__'

class CompetenciaSerializer(serializers.ModelSerializer):

    curso = CursoSerializer(read_only=True)

    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), source='curso', write_only=True
    )

    class Meta:
        model = Competencia
        fields = '__all__'

class HabilidadeSerializer(serializers.ModelSerializer):

    curso = CursoSerializer(read_only=True)

    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), source='curso', write_only=True
    )

    class Meta:
        model = Habilidade
        fields = '__all__'
