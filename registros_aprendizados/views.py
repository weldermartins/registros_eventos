from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topico, Assuntos
from .forms import TopicoForm, AssuntosForm


def index(request):
    """A página inicial do registros de aprendizados"""
    return render(request, 'registros_aprendizados/index.html')

@login_required
def topicos(requisicao):
    """Mostra todos os tópicos."""
    topicos = Topico.objects.filter(owner=requisicao.user).order_by('data')
    contexto = {'topicos': topicos}
    return render(requisicao, 'registros_aprendizados/topicos.html', contexto)


@login_required
def topico(requisicao, topico_id):
    """Mostra um único tópico e todas as seus assuntos."""            
    topico = Topico.objects.get(id=topico_id)
    # Garante que o assunto pertence ao usuário atual
    if topico.owner != requisicao.user:
        raise Http404

    assuntos = topico.assuntos_set.order_by('-data')
    contexto = {'topico': topico, 'assuntos': assuntos}
    return render(requisicao, 'registros_aprendizados/topico.html', contexto)

    
# Toda requisição inicia-se com get, se for get gera um formulário vazio(33), carrega no contexto
# e retorna o formulário sem dados para preencher(43)
@login_required
def novo_topico(requisicao):
    """Adiciona um novo assunto."""
    if requisicao.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicoForm()
    else:
        # Dados de post submetidos; processa os dados
        form = TopicoForm(requisicao.POST)
        if form.is_valid():
            # Não salva antes de owner receber o ID da do usuário logado.
            novo_topico = form.save(commit=False)
            novo_topico.owner = requisicao.user
            novo_topico.save()
            # procura a url tópicos
            return HttpResponseRedirect(reverse('registros_aprendizados:topicos'))
    contexto = {'form': form}
    return render(requisicao, 'registros_aprendizados/novo_topico.html', contexto)


@login_required
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


@login_required
def editar_assunto(requisicao, assunto_id):
    """Edita uma entrada existente."""
    assunto = Assuntos.objects.get(id=assunto_id)
    # vincula o assunto ao id do topico.
    topico = assunto.topico
    if topico.owner != requisicao.user:
        raise Http404

    if requisicao.method != 'POST':
        # Requisição inicial; preeche previamente o formulário com a entrada atual
        form = AssuntosForm(instance=assunto)
    else:
        # dados de POST submetidos; processa os dados
        form = AssuntosForm(instance=assunto, data=requisicao.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registros_aprendizados:topico', args=[topico.id]))
    contexto = {'assunto': assunto, 'topico': topico, 'form': form}
    return render(requisicao, 'registros_aprendizados/editar_assunto.html', contexto)

@login_required
def editar_topico(requisicao, topico_id):
    """Edita uma entrada existente."""
    topico = Topico.objects.get(id=topico_id)
    if topico.owner != requisicao.user:
        raise Http404

    if requisicao.method != 'POST':
        # Requisição inicial; preeche previamente o formulário com a entrada atual
        form = TopicoForm(instance=topico)
    else:
        # dados de POST submetidos; processa os dados
        form = TopicoForm(instance=topico, data=requisicao.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('registros_aprendizados:topico', args=[topico.id]))
    contexto = {'topico': topico, 'form': form}
    return render(requisicao, 'registros_aprendizados/editar_topico.html', contexto)


def excluir_assunto(requisicao, assunto_id):
    assunto = Assuntos.objects.get(id=assunto_id)
    topico = assunto.topico
    contexto = {'assunto': assunto}

    if requisicao.method == 'POST':
        assunto.delete()
        return HttpResponseRedirect(reverse('registros_aprendizados:topico',  args=[topico.id]))
    return render(requisicao, 'registros_aprendizados/excluir_assunto.html', contexto)
