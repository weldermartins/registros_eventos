from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topico
from .forms import TopicoForm, AssuntosForm


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

    
# Toda requisição inicia-se com get, se for get gera um formulário vazio(33), carrega no contexto
# e retorna o formulário sem dados para preencher(43)
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
            # procura a url tópicos
            return HttpResponseRedirect(reverse('registros_aprendizados:topicos'))
    contexto = {'form': form}
    return render(requisicao, 'registros_aprendizados/novo_topico.html', contexto)


def novo_assunto(requisicao, topico_id):
    """Acrescenta um novo assunto para um tópico em particular."""
    topico = Topico.objects.get(id=topico_id)

    if requisicao.method != 'POST':
        # Nenhum dados submetido; cria um formulário em branco
        form = AssuntosForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = AssuntosForm(data=requisicao.POST)
        if form.is_valid():
            # não permite salvar no banco sem concluir os demais comandos
            novo_assunto = form.save(commit=False)
            # vincula o assunto ao id do topico.
            novo_assunto.topico = topico
            novo_assunto.save()
        return HttpResponseRedirect(reverse('registros_aprendizados:topico', args=[topico_id]))

    contexto = {'topico': topico, 'form': form}
    return render(requisicao, 'registros_aprendizados/novo_assunto.html', contexto)

def 

