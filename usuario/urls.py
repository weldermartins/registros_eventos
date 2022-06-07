from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'usuario'

urlpatterns = [
    # Página para logar
    path('login/',
         auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),

    # Sair da página
    path('/sair/', views.logout_view, name='sair'),

    ]
