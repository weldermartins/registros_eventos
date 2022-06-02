from django.shortcuts import render
from .models import Topico

def index(request):
    """A página inicial do registros de aprendizados"""
    return render(request, 'registros_aprendizados/index.html')

def topicos(requisicao):
    """Mostra todos os tópicos."""
    topicos = Topico.objects.order_by('data')
    contexto = {'topicos': topicos}
    return render(requisicao, 'registros_aprendizados/topicos.html', contexto)


def topico(requisicao, topico_id):
    """Mostra um único tópico e todas as seus assuntos."""            
    topico = Topico.objects.get(id=topico_id)
    assuntos = topico.assuntos_set.order_by('-data')
    contexto = {'topico': topico, 'assuntos': assuntos'}
    return render(requisicao, 'registros_aprendizados/topico.html', contexto)
    
    
