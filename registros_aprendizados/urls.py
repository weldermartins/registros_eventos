"""Define padrões de url para registros_aprendizados"""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial.
    # Diz ao python para procurar uma url sem nada entre o início
    # e o fim da url.
    path('', views.home, name='index'),

    ]    