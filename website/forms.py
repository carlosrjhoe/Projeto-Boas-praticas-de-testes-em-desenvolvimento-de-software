from django import forms
from .models import Funcionario


class InsereFuncionarioForm(forms.Form):
    class Meta:

        model = Funcionario
        
        fields = [
            'nome',
            'sobre_nome',
            'cpf',
            'remuneracao',
            'tempo_de_servico',
        ]
        
        exclude = [
            'tempo_de_servico'
        ]
