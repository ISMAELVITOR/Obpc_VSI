from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.indisponibilidade import Indisponibilidade
from app.forms.indisponibilidade_form import IndisponibilidadeForm
from app.views.base_view import ProtectedView


# Listagem de Indisponibilidades
class IndisponibilidadeListView(ProtectedView, ListView):
    model = Indisponibilidade
    template_name = "indisponibilidade/indisponibilidade_listar.html"
    context_object_name = "indisponibilidades"
    ordering = ['data']


# Criação de Indisponibilidade
class IndisponibilidadeCreateView(ProtectedView, CreateView):
    model = Indisponibilidade
    form_class = IndisponibilidadeForm
    template_name = "indisponibilidade/indisponibilidade_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Indisponibilidade criada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_indisponibilidade")


# Edição de Indisponibilidade
class IndisponibilidadeUpdateView(ProtectedView, UpdateView):
    model = Indisponibilidade
    form_class = IndisponibilidadeForm
    template_name = "indisponibilidade/indisponibilidade_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Indisponibilidade atualizada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_indisponibilidade")


# Exclusão de Indisponibilidade
class IndisponibilidadeDeleteView(ProtectedView, DeleteView):
    model = Indisponibilidade
    template_name = "indisponibilidade/indisponibilidade_delete_confirm.html"
    context_object_name = "indisponibilidade"
    success_url = reverse_lazy("listar_indisponibilidade")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Indisponibilidade deletada com sucesso!")
        return super().delete(request, *args, **kwargs)

