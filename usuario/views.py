from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def logout_view(requisicao):
    """Faz logout do usuário."""
    logout(requisicao)
    return HttpResponseRedirect(reverse('registros_aprendizados:index'))




