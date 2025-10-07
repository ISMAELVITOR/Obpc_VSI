from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.funcao import Funcao
from app.forms.funcao_form import FuncaoForm
from app.views.base_view import ProtectedView


# Listagem de Funções
class FuncaoListView(ProtectedView, ListView):
    model = Funcao
    template_name = "funcao/funcao_listar.html"
    context_object_name = "funcoes"
    ordering = ['nome']


# Criação de Função
class FuncaoCreateView(ProtectedView, CreateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = "funcao/funcao_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Função criada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_funcao")


# Edição de Função
class FuncaoUpdateView(ProtectedView, UpdateView):
    model = Funcao
    form_class = FuncaoForm
    template_name = "funcao/funcao_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Função atualizada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_funcao")


# Exclusão de Função
class FuncaoDeleteView(ProtectedView, DeleteView):
    model = Funcao
    template_name = "funcao/funcao_delete_confirm.html"
    context_object_name = "funcao"
    success_url = reverse_lazy("listar_funcao")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Função deletada com sucesso!")
        return super().delete(request, *args, **kwargs)

