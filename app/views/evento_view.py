from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.evento import Evento
from app.forms.evento_form import EventoForm
from app.views.base_view import ProtectedView


# Listagem de Eventos
class EventoListView(ProtectedView, ListView):
    model = Evento
    template_name = "evento/evento_listar.html"
    context_object_name = "eventos"
    ordering = ['data_inicio', 'hora_inicio']


# Criação de Evento
class EventoCreateView(ProtectedView, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "evento/evento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Evento criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_evento")


# Edição de Evento
class EventoUpdateView(ProtectedView, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = "evento/evento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Evento atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_evento")


# Exclusão de Evento
class EventoDeleteView(ProtectedView, DeleteView):
    model = Evento
    template_name = "evento/evento_delete_confirm.html"
    context_object_name = "evento"
    success_url = reverse_lazy("listar_evento")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Evento deletado com sucesso!")
        return super().delete(request, *args, **kwargs)

