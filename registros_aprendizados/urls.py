"""Define padrões de url para registros_aprendizados"""
from django.urls import path
from . import views

app_name = 'registros_aprendizados'

urlpatterns = [
    # Página inicial.
    # Diz ao python para procurar uma url sem nada entre o início
    # e o fim da url.
    path('', views.index, name='index'),

    ]    