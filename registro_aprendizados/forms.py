from django import forms

from .models import Topico, Assuntos


class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['texto']
        # Não gera rotolo.
        labels = {'texto': ''}


class AssuntosForm(forms.ModelForm):
    class Meta:
        model = Assuntos
        fields = ['assunto']
        labels = {'assunto': ''}
        # 80 colunas ao invés de 40 conforme o padrão.
        widgets = {'assunto': forms.Textarea(attrs={'cols': 80})}
