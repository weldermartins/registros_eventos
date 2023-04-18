from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(requisicao):
    """Faz logout do usuário."""
    logout(requisicao)
    return HttpResponseRedirect(reverse('registro_aprendizados:index'))


def cadastro(requisicao):
    """Faz o cadastro de um novo usuário."""
    if requisicao.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # processa o formulário preenchido
        form = UserCreationForm(data=requisicao.POST)

        if form.is_valid():
            novo_usuario = form.save()
            # Faz login de usuário e o redireciona para a página inicial
            usuario_autenticado = authenticate(username=novo_usuario.usernamame, password=requisicao.post['password1'])
            login(requisicao, usuario_autenticado)
            return HttpResponseRedirect(reverse('registro_aprendizados:index'))

    contexto = {'form': form}
    return render(requisicao, 'usuario/cadastro.html', contexto)






