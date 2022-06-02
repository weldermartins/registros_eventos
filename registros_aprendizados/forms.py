from django import forms

from .models import Topico


class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['texto']
        # Não gera rotolo.
        labels = {'texto': ''}
