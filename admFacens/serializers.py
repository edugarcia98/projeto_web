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

class CursoDisciplinaSerializer(serializers.ModelSerializer):

    curso = CursoSerializer(read_only=True)

    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), source='curso', write_only=True
    )

    disciplina = DisciplinaSerializer(read_only=True)

    disciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=Disciplina.objects.all(), source='disciplina', write_only=True
    )

    class Meta:
        model = CursoDisciplina
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    class Meta:
        model = Turma
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    class Meta:
        model = Livro
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):

    turma = TurmaSerializer(read_only=True)

    turma_id = serializers.PrimaryKeyRelatedField(
        queryset=Turma.objects.all(), source='turma', write_only=True
    )

    class Meta:
        model = Aula
        fields = '__all__'