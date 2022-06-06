"""Define padrões de url para registros_aprendizados"""
from django.urls import path
from . import views

app_name = 'registros_aprendizados'

urlpatterns = [
    # Página inicial.
    # Diz ao python para procurar uma url sem nada entre o início
    # e o fim da url.
    path('', views.index, name='index'),
    
    # Mostra todos os tópicos
    path('topicos/', views.topicos, name='topicos'),
    
    # Mostra um tópico individual por id e seus assuntos
    path('topico/<int:topico_id>', views.topico, name='topico'),

    # Pagina para adicinar um novo tópico
    path('novo_topico/', views.novo_topico, name='novo_topico'),

    # Novos assuntos
    path('novo_assunto/<int:topico_id>/', views.novo_assunto, name='novo_assunto'),

    # Editando entradas
    path('editar_assunto/<int:editar_assunto>/', views.editar_assunto, name="editar_assunto")

    ]
