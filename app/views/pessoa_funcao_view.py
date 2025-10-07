from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.pessoa_funcao import PessoaFuncao
from app.forms.pessoa_funcao_form import PessoaFuncaoForm
from app.views.base_view import ProtectedView

# Listagem
class PessoaFuncaoListView(ProtectedView, ListView):
    model = PessoaFuncao
    template_name = "pessoa_funcao/pessoa_funcao_listar.html"
    context_object_name = 'pessoa_funcoes'
    ordering = ['pessoa__nome', 'funcao__nome']

# Criação
class PessoaFuncaoCreateView(ProtectedView, CreateView):
    model = PessoaFuncao
    form_class = PessoaFuncaoForm
    template_name = "pessoa_funcao/pessoa_funcao_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Vínculo criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_pessoa_funcao')

# Edição
class PessoaFuncaoUpdateView(ProtectedView, UpdateView):
    model = PessoaFuncao
    form_class = PessoaFuncaoForm
    template_name = "pessoa_funcao/pessoa_funcao_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Vínculo atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_pessoa_funcao')

# Exclusão
class PessoaFuncaoDeleteView(ProtectedView, DeleteView):
    model = PessoaFuncao
    template_name = "pessoa_funcao/pessoa_funcao_delete_confirm.html"
    context_object_name = 'pessoa_funcao'
    success_url = reverse_lazy('listar_pessoa_funcao')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Vínculo removido com sucesso!")
        return super().delete(request, *args, **kwargs)

