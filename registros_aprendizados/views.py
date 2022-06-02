from django.shortcuts import render

def home(request):
    """A página inicial do registros de aprendizados"""
    return render(request, 'registros_aprendizados/home.html')
