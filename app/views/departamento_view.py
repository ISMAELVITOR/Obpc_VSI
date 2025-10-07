from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.departamento import Departamento
from app.forms.departamento_form import DepartamentoForm
from app.views.base_view import ProtectedView  


# Listagem de Departamentos
class DepartamentoListView(ProtectedView, ListView):
    model = Departamento
    template_name = "departamento/departamento_listar.html"
    context_object_name = 'departamentos'
    ordering = ['nome']


# Criação de Departamento
class DepartamentoCreateView(ProtectedView, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "departamento/departamento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Departamento criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_departamento')


# Edição de Departamento
class DepartamentoUpdateView(ProtectedView, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "departamento/departamento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Departamento atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_departamento')


# Exclusão de Departamento
class DepartamentoDeleteView(ProtectedView, DeleteView):
    model = Departamento
    template_name = "departamento/departamento_delete_confirm.html"
    context_object_name = 'departamento'
    success_url = reverse_lazy('listar_departamento')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Departamento deletado com sucesso!")
        return super().delete(request, *args, **kwargs)

