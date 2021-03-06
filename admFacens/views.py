from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

class ObjetivoViewSet(viewsets.ModelViewSet):

    serializer_class = ObjetivoSerializer
    queryset = Objetivo.objects.all()

class CompetenciaViewSet(viewsets.ModelViewSet):

    serializer_class = CompetenciaSerializer
    queryset = Competencia.objects.all()

class HabilidadeViewSet(viewsets.ModelViewSet):
    serializer_class = HabilidadeSerializer
    queryset = Habilidade.objects.all()

class CursoViewSet(viewsets.ModelViewSet):

    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class DisciplinaViewSet(viewsets.ModelViewSet):

    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all()

class CursoDisciplinaViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaSerializer
    queryset = CursoDisciplina.objects.all()

class CursoDisciplinaLivroViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaLivroSerializer
    queryset = CursoDisciplinaLivro.objects.all()

class CursoDisciplinaObjetivoViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaObjetivoSerializer
    queryset = CursoDisciplinaObjetivo.objects.all()

class CursoDisciplinaCompetenciaViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaCompetenciaSerializer
    queryset = CursoDisciplinaCompetencia.objects.all()

class CursoDisciplinaHabilidadeViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaHabilidadeSerializer
    queryset = CursoDisciplinaHabilidade.objects.all()

class TurmaViewSet(viewsets.ModelViewSet):

    serializer_class = TurmaSerializer
    queryset = Turma.objects.all()

class ConteudoViewSet(viewsets.ModelViewSet):

    serializer_class = ConteudoSerializer
    queryset = Conteudo.objects.all()

class MetodologiaEnsinoViewSet(viewsets.ModelViewSet):

    serializer_class = MetodologiaEnsinoSerializer
    queryset = MetodologiaEnsino.objects.all()

class LivroViewSet(viewsets.ModelViewSet):

    serializer_class = LivroSerializer
    queryset = Livro.objects.all()

class AulaViewSet(viewsets.ModelViewSet):

    serializer_class = AulaSerializer
    queryset = Aula.objects.all()

class RegisterViewSet(viewsets.ModelViewSet):

    serializer_class = RegisterSerializer
    queryset = Register.objects.all()