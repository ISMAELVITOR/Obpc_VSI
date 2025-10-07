from django import forms
from app.models.pessoa_funcao import PessoaFuncao

class PessoaFuncaoForm(forms.ModelForm):
    class Meta:
        model = PessoaFuncao
        fields = ['pessoa', 'funcao']

