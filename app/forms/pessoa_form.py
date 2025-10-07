from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Pessoa

class PessoaForm(forms.ModelForm):
    # Removemos a senha do form padrão, será usada apenas na criação
    class Meta:
        model = Pessoa
        fields = ["nome", "data_nascimento", "cpf", "rg", "email", "perfil"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"})
        }


# Form separado apenas para registro
class PessoaRegisterForm(UserCreationForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "data_nascimento", "cpf", "rg", "email", "perfil", "password1", "password2"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"})
        }


