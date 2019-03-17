from django.contrib import admin
from .models import *

# Register your models here.

#Classes:

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

class LivroAdmin(admin.ModelAdmin):
    fields = ['title', 'autor', 'bibliografia']
    list_display = ['title', 'autor', 'bibliografia']

class DisciplinaAdmin(admin.ModelAdmin):
    fields = ['title', 'tipo', 'creditos']
    list_display = ['title', 'tipo', 'creditos', 'horas_aula']

class DisciplinaInline(admin.TabularInline):
    model = Curso.disciplinas.through
    exclude = ['objetivos', 'competencias', 'habilidades']
    extra = 1
    verbose_name = "Disciplina"
    verbose_name_plural = "Disciplinas"
    classes = ['collapse']

class CursoAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    inlines = [ObjetivoInline, CompetenciaInline, HabilidadeInline, DisciplinaInline]
    list_display = ['title', 'description']

"""
class CursoDisciplinaObjetivoInline(admin.TabularInline):
    model = CursoDisciplina.objetivos.through
    extra = 1
    verbose_name = "Objetivo"
    verbose_name_plural = "Objetivos"
    classes = ['collapse']

class CursoDisciplinaCompetenciaInline(admin.TabularInline):
    model = CursoDisciplina.competencias.through
    extra = 1
    verbose_name = "Competencia"
    verbose_name_plural = "Competencias"
    classes = ['collapse']

class CursoDisciplinaHabilidadeInline(admin.TabularInline):
    model = CursoDisciplina.habilidades.through
    extra = 1
    verbose_name = "Habilidade"
    verbose_name_plural = "Habilidades"
    classes = ['collapse']
"""

class TurmaInline(admin.TabularInline):
    model = CursoDisciplina.turmas.through
    extra = 1
    verbose_name="Turma"
    verbose_name_plural="Turmas"
    classes = ['collapse']

class AulaInline(admin.TabularInline):
    model = CursoDisciplinaTurma.aulas.through
    extra = 1
    verbose_name="Aula"
    verbose_name_plural="Aulas"
    classes = ['collapse']

class CursoDisciplinaLivroInline(admin.TabularInline):
    model = CursoDisciplina.livros.through
    extra = 1
    verbose_name="Livro"
    verbose_name_plural="Livros"
    classes = ['collapse']

class CursoDisciplinaTurmaAulaLivroInline(admin.TabularInline):
    model = CursoDisciplinaTurmaAula.livros.through
    extra = 1
    verbose_name="Livro"
    verbose_name_plural="Livros"
    classes = ['collapse']

class CursoDisciplinaAdmin(admin.ModelAdmin):
    fields = ['curso', 'disciplina']
    #inlines = [CursoDisciplinaObjetivoInline, CursoDisciplinaCompetenciaInline, CursoDisciplinaHabilidadeInline]
    inlines = [TurmaInline, CursoDisciplinaLivroInline]
    list_display = ['curso', 'disciplina']

class CursoDisciplinaTurmaAdmin(admin.ModelAdmin):
    fields = ['cursoDisciplina', 'turma']
    inlines = [AulaInline]
    list_display = ['cursoDisciplina', 'turma']

class CursoDisciplinaTurmaAulaAdmin(admin.ModelAdmin):
    fields = ['cursoDisciplinaTurma', 'aula']
    inlines = [CursoDisciplinaTurmaAulaLivroInline]
    list_display = ['cursoDisciplinaTurma', 'aula']


#Registros do Admin

admin.site.register(Objetivo, ObjetivoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Habilidade, HabilidadeAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(CursoDisciplina, CursoDisciplinaAdmin)
admin.site.register(CursoDisciplinaTurma, CursoDisciplinaTurmaAdmin)
admin.site.register(CursoDisciplinaTurmaAula, CursoDisciplinaTurmaAulaAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Turma)
admin.site.register(Aula)
