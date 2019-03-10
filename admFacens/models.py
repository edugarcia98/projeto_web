from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Semestre(models.Model):
    number = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)], verbose_name = "Semestre")
    year = models.IntegerField(validators = [MinValueValidator(1900)], verbose_name = "Ano")

    def __str__(self):
        return str(self.number) + "/" + str(self.year)

    class Meta:
        ordering = ('number',)

class Objetivo(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Objetivo")
    description = models.CharField(max_length = 1000, verbose_name = "Descricao")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Competencia(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Competencia")
    description = models.CharField(max_length = 1000, verbose_name = "Descricao")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Habilidade(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Habilidade")
    description = models.CharField(max_length = 1000, verbose_name = "Descricao")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Curso(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Curso")
    description = models.CharField(max_length = 1000, verbose_name = "Descricao")
    semestres = models.ManyToManyField(Semestre)
    objetivos = models.ManyToManyField(Objetivo)
    competencias = models.ManyToManyField(Competencia)
    habilidades = models.ManyToManyField(Habilidade)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)