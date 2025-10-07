from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.escala import Escala
from app.forms.escala_form import EscalaForm
from app.views.base_view import ProtectedView

# Listagem
class EscalaListView(ProtectedView, ListView):
    model = Escala
    template_name = "escala/escala_listar.html"
    context_object_name = 'escalas'
    ordering = ['evento__nome', 'funcao__nome']  # removido 'data'

# Criação
class EscalaCreateView(ProtectedView, CreateView):
    model = Escala
    form_class = EscalaForm
    template_name = "escala/escala_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Escala criada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_escala')

# Edição
class EscalaUpdateView(ProtectedView, UpdateView):
    model = Escala
    form_class = EscalaForm
    template_name = "escala/escala_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Escala atualizada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('listar_escala')

# Exclusão
class EscalaDeleteView(ProtectedView, DeleteView):
    model = Escala
    template_name = "escala/escala_delete_confirm.html"
    context_object_name = 'escala'
    success_url = reverse_lazy('listar_escala')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Escala deletada com sucesso!")
        return super().delete(request, *args, **kwargs)

