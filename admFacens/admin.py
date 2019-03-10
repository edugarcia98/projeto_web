from django.contrib import admin
from .models import *

# Register your models here.

#Classes:

class SemestreAdmin(admin.ModelAdmin):
    fields = ['number', 'year']
    list_display = ('number', 'year')
    list_filter = ['year']

class SemestreInline(admin.TabularInline):
    model = Curso.semestres.through
    extra = 1
    verbose_name = "Semestre"
    verbose_name_plural = "Semestres"
    classes = ['collapse']
    
class ObjetivoAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ('title', 'description')

class ObjetivoInline(admin.TabularInline):
    model = Curso.objetivos.through
    extra = 1
    verbose_name = "Objetivo"
    verbose_name_plural = "Objetivos"
    classes = ['collapse']

class CompetenciaAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ('title', 'description')

class CompetenciaInline(admin.TabularInline):
    model = Curso.competencias.through
    extra = 1
    verbose_name = "Competencia"
    verbose_name_plural = "Competencias"
    classes = ['collapse']

class HabilidadeAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ('title', 'description')

class HabilidadeInline(admin.TabularInline):
    model = Curso.habilidades.through
    extra = 1
    verbose_name = "Habilidade"
    verbose_name_plural = "Habilidades"
    classes = ['collapse']

class CursoAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    inlines = [SemestreInline, ObjetivoInline, CompetenciaInline, HabilidadeInline]
    list_display = ['title', 'description']

#Registros do Admin

admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Objetivo, ObjetivoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Habilidade, HabilidadeAdmin)
admin.site.register(Curso, CursoAdmin)