from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .models import Objetivo
from .serializers import ObjetivoSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

class ObjetivoViewSet(viewsets.ModelViewSet):

    serializer_class = ObjetivoSerializer
    queryset = Objetivo.objects.all()
