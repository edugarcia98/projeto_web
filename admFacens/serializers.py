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

class LivroSerializer(serializers.ModelSerializer):

    #cursoDisciplina = CursoDisciplinaSerializer(read_only=True)
#
    #cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
    #    queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    #)

    class Meta:
        model = Livro
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

class CursoDisciplinaLivroSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    livro = LivroSerializer(read_only=True)

    livro_id = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), source='livro', write_only=True
    )

    class Meta:
        model = CursoDisciplinaLivro
        fields = '__all__'

class CursoDisciplinaObjetivoSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    objetivo = ObjetivoSerializer(read_only=True)

    objetivo_id = serializers.PrimaryKeyRelatedField(
        queryset=Objetivo.objects.all(), source='objetivo', write_only=True
    )

    class Meta:
        model = CursoDisciplinaObjetivo
        fields = '__all__'

class CursoDisciplinaCompetenciaSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    competencia = CompetenciaSerializer(read_only=True)

    competencia_id = serializers.PrimaryKeyRelatedField(
        queryset=Competencia.objects.all(), source='competencia', write_only=True
    )

    class Meta:
        model = CursoDisciplinaCompetencia
        fields = '__all__'

class CursoDisciplinaHabilidadeSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    habilidade = HabilidadeSerializer(read_only=True)

    habilidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Habilidade.objects.all(), source='habilidade', write_only=True
    )

    class Meta:
        model = CursoDisciplinaHabilidade
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    class Meta:
        model = Turma
        fields = '__all__'

class ConteudoSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    class Meta:
        model = Conteudo
        fields = '__all__'

class MetodologiaEnsinoSerializer(serializers.ModelSerializer):

    cursoDisciplina = CursoDisciplinaSerializer(read_only=True)

    cursoDisciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=CursoDisciplina.objects.all(), source='cursoDisciplina', write_only=True
    )

    class Meta:
        model = MetodologiaEnsino
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):

    turma = TurmaSerializer(read_only=True)

    turma_id = serializers.PrimaryKeyRelatedField(
        queryset=Turma.objects.all(), source='turma', write_only=True
    )

    class Meta:
        model = Aula
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = '__all__'