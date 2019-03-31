from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

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

class Disciplina(models.Model):
    DISC_TYPES = (
        ('T', 'Teorica'),
        ('P', 'Pratica'),
    )

    CREDITO_TYPES = (
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
    )

    title = models.CharField(max_length=100, verbose_name="Disciplina")
    tipo = models.CharField(max_length=1, choices=DISC_TYPES, verbose_name="Tipo")
    creditos = models.IntegerField(choices=CREDITO_TYPES, verbose_name="Creditos")

    def _get_horas_aula(self):
        return self.creditos * 20

    horas_aula = property(_get_horas_aula)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Turma(models.Model):
    codigo = models.CharField(max_length=10, verbose_name="Codigo")

    def __str__(self):
        return self.codigo

    class Meta:
        ordering = ('codigo',)

class Aula(models.Model):
    AULA_TYPES = (
        ('T', 'Teorica'),
        ('P', 'Pratica'),
        ('-', 'Nenhum'),
    )

    semana = models.IntegerField(validators = [MinValueValidator(1)], verbose_name="Semana")
    data = models.DateField(verbose_name="Data")
    tipo = models.CharField(max_length=1, choices=AULA_TYPES, verbose_name="Tipo")
    conteudo = models.CharField(max_length=100, verbose_name="Conteudo")

    def __str__(self):
        return self.conteudo

    class Meta:
        ordering = ('conteudo',)

class Livro(models.Model):
    LIVRO_TYPES = (
        ('B', 'Basica'),
        ('C', 'Complementar'),
    )

    title = models.CharField(max_length=200, verbose_name="Titulo")
    autor = models.CharField(max_length=500, verbose_name="Autor(es)")
    bibliografia = models.CharField(max_length=1, choices=LIVRO_TYPES, verbose_name="Bibliografia")

    def __str__(self):
        return self.title + " - " + self.autor

    class Meta:
        ordering = ('title',)

class Curso(models.Model):
    title = models.CharField(max_length=50, verbose_name="Curso")
    description = models.CharField(max_length=1000, verbose_name="Descricao")
    objetivos = models.ManyToManyField(Objetivo, through='CursoObjetivo')
    competencias = models.ManyToManyField(Competencia, through='CursoCompetencia')
    habilidades = models.ManyToManyField(Habilidade, through='CursoHabilidade')
    disciplinas = models.ManyToManyField(Disciplina, through='CursoDisciplina')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class CursoObjetivo(models.Model):
    curso = models.ForeignKey(Curso, null=False, on_delete=models.CASCADE)
    objetivo = models.ForeignKey(Objetivo, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso.title + " - " + self.objetivo.title

class CursoCompetencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso.title + " - " + self.competencia.title

class CursoHabilidade(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    habilidade = models.ForeignKey(Habilidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso.title + " - " + self.habilidade.title

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    objetivos = models.ManyToManyField(CursoObjetivo, blank=True)
    competencias = models.ManyToManyField(CursoCompetencia, blank=True)
    habilidades = models.ManyToManyField(CursoHabilidade, blank=True)
    turmas = models.ManyToManyField(Turma, through='CursoDisciplinaTurma')
    livros = models.ManyToManyField(Livro, through='CursoDisciplinaLivro')

    def __str__(self):
        return self.curso.title + " - " + self.disciplina.title

class CursoDisciplinaTurma(models.Model):
    cursoDisciplina = models.ForeignKey(CursoDisciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aulas = models.ManyToManyField(Aula, through='CursoDisciplinaTurmaAula')

    def __str__(self):
        return self.turma.codigo

class CursoDisciplinaLivro(models.Model):
    cursoDisciplina = models.ForeignKey(CursoDisciplina, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cursoDisciplina) + " - " + str(self.livro)

class CursoDisciplinaTurmaAula(models.Model):
    cursoDisciplinaTurma = models.ForeignKey(CursoDisciplinaTurma, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    livros = models.ManyToManyField(CursoDisciplinaLivro)

    def __str__(self):
        return str(self.cursoDisciplinaTurma) + " - " + str(self.aula)


"""
class Semestre(models.Model):
    number = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)], verbose_name = "Semestre")
    year = models.IntegerField(validators = [MinValueValidator(1900)], verbose_name = "Ano")

    def __str__(self):
        return str(self.number) + "/" + str(self.year)

    class Meta:
        ordering = ('number',)

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
"""