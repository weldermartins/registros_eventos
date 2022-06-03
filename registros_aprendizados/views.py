from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topico
from .forms import TopicoForm


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
    contexto = {'topico': topico, 'assuntos': assuntos}
    return render(requisicao, 'registros_aprendizados/topico.html', contexto)
    

def novo_topico(requisicao):
    """Adiciona um novo assunto."""
    if requisicao.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicoForm()
    else:
        # Dados de post submetidos; processa os dados
        form = TopicoForm(requisicao.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registros_aprendizados:topicos'))
    contexto = {'form': form}
    return render(requisicao, 'registros_aprendizados/novo_topico.html', contexto)

