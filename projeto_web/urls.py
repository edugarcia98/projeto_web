"""projeto_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from admFacens.views import *

router = routers.DefaultRouter()
router.register('objetivo', ObjetivoViewSet, base_name='objetivo')
router.register('competencia', CompetenciaViewSet, base_name='competencia')
router.register('habilidade', HabilidadeViewSet, base_name='habilidade')
router.register('curso', CursoViewSet, base_name='curso')
router.register('disciplina', DisciplinaViewSet, base_name='disciplina')
router.register('curso-disciplina', CursoDisciplinaViewSet, base_name='curso-disciplina')
router.register('turma', TurmaViewSet, base_name='turma')
router.register('conteudo', ConteudoViewSet, base_name='conteudo')
router.register('metodologia-ensino', MetodologiaEnsinoViewSet, base_name='metodologia-ensino')
router.register('livro', LivroViewSet, base_name='livro')
router.register('curso-disciplina-livro', CursoDisciplinaLivroViewSet, base_name='curso-disciplina-livro')
router.register('curso-disciplina-objetivo', CursoDisciplinaObjetivoViewSet, base_name='curso-disciplina-objetivo')
router.register('curso-disciplina-competencia', CursoDisciplinaCompetenciaViewSet, base_name='curso-disciplina-competencia')
router.register('curso-disciplina-habilidade', CursoDisciplinaHabilidadeViewSet, base_name='curso-disciplina-habilidade')
router.register('aula', AulaViewSet, base_name='aula')
router.register('register', RegisterViewSet, base_name='register')

urlpatterns = [
    path('admFacens/', include('admFacens.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
