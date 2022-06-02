from django.shortcuts import render

def index(request):
    """A página inicial do registros de aprendizados"""
    return render(request, 'registros_aprendizados/index.html')
