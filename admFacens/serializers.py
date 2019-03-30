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