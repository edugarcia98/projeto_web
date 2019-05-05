from django.contrib import admin
from .models import *

# Register your models here.

#Classes:

class ObjetivoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'curso']
    list_display = ('title', 'description', 'curso')

#class ObjetivoInline(admin.TabularInline):
#    model = Curso.objetivos.through
#    extra = 1
#    verbose_name = "Objetivo"
#    verbose_name_plural = "Objetivos"
#    classes = ['collapse']

class CompetenciaAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'curso']
    list_display = ('title', 'description', 'curso')

#class CompetenciaInline(admin.TabularInline):
#    model = Curso.competencias.through
#    extra = 1
#    verbose_name = "Competencia"
#    verbose_name_plural = "Competencias"
#    classes = ['collapse']

class HabilidadeAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'curso']
    list_display = ('title', 'description', 'curso')

#class HabilidadeInline(admin.TabularInline):
#    model = Curso.habilidades.through
#    extra = 1
#    verbose_name = "Habilidade"
#    verbose_name_plural = "Habilidades"
#    classes = ['collapse']

class DisciplinaAdmin(admin.ModelAdmin):
    fields = ['title', 'tipo', 'creditos', 'ementa']
    list_display = ['title', 'tipo', 'creditos', 'horas_aula', 'ementa']

class DisciplinaInline(admin.TabularInline):
    model = Curso.disciplinas.through
    exclude = ['objetivos', 'competencias', 'habilidades']
    extra = 1
    verbose_name = "Disciplina"
    verbose_name_plural = "Disciplinas"
    classes = ['collapse']

class CursoAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    inlines = [DisciplinaInline]
    list_display = ['title', 'description']


#class TurmaInline(admin.TabularInline):
#    model = CursoDisciplina.turmas.through
#    extra = 1
#    verbose_name="Turma"
#    verbose_name_plural="Turmas"
#    classes = ['collapse']

#class AulaInline(admin.TabularInline):
#    model = CursoDisciplinaTurma.aulas.through
#    extra = 1
#    verbose_name="Aula"
#    verbose_name_plural="Aulas"
#    classes = ['collapse']

#class CursoDisciplinaLivroInline(admin.TabularInline):
#    model = CursoDisciplina.livros.through
#    extra = 1
#    verbose_name="Livro"
#    verbose_name_plural="Livros"
#    classes = ['collapse']

#class CursoDisciplinaTurmaAulaLivroInline(admin.TabularInline):
#    model = CursoDisciplinaTurmaAula.livros.through
#    extra = 1
#    verbose_name="Livro"
#    verbose_name_plural="Livros"
#    classes = ['collapse']

class CursoDisciplinaAdmin(admin.ModelAdmin):
    fields = ['curso', 'disciplina']
    list_display = ['curso', 'disciplina']




#Registros do Admin

admin.site.register(Objetivo, ObjetivoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Habilidade, HabilidadeAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(CursoDisciplina, CursoDisciplinaAdmin)
admin.site.register(Livro)
admin.site.register(Turma)
admin.site.register(Conteudo)
admin.site.register(MetodologiaEnsino)
admin.site.register(Aula)
admin.site.register(CursoDisciplinaLivro)
admin.site.register(CursoDisciplinaObjetivo)
admin.site.register(CursoDisciplinaCompetencia)
admin.site.register(CursoDisciplinaHabilidade)
