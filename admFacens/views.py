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

class TurmaViewSet(viewsets.ModelViewSet):

    serializer_class = TurmaSerializer
    queryset = Turma.objects.all()

class CursoDisciplinaViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaSerializer
    queryset = CursoDisciplina.objects.all()

class CursoDisciplinaTurmaViewSet(viewsets.ModelViewSet):

    serializer_class = CursoDisciplinaTurmaSerializer
    queryset = CursoDisciplinaTurma.objects.all()