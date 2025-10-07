from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models.pessoa import Pessoa
from app.forms.pessoa_form import PessoaForm
from app.views.base_view import ProtectedView


# Listagem de Pessoas
class PessoaListView(ProtectedView, ListView):
    model = Pessoa
    template_name = "pessoa/pessoa_listar.html"
    context_object_name = "pessoas"
    ordering = ['id']


# Criação de Pessoa
class PessoaCreateView(ProtectedView, CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/pessoa_criar.html"

    def form_valid(self, form):
        pessoa = form.save(commit=False)
        # Aplica senha apenas se o campo estiver preenchido
        if form.cleaned_data.get("password"):
            pessoa.set_password(form.cleaned_data["password"])
        pessoa.save()
        messages.success(self.request, "Pessoa criada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_pessoas")


# Edição de Pessoa
class PessoaUpdateView(ProtectedView, UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/pessoa_criar.html"

    def form_valid(self, form):
        pessoa = form.save(commit=False)
        if form.cleaned_data.get("password"):
            pessoa.set_password(form.cleaned_data["password"])
        pessoa.save()
        messages.success(self.request, "Pessoa atualizada com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("listar_pessoas")


# Exclusão de Pessoa
class PessoaDeleteView(ProtectedView, DeleteView):
    model = Pessoa
    template_name = "pessoa/pessoa_deletar.html"
    context_object_name = "pessoa"
    success_url = reverse_lazy("listar_pessoas")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Pessoa deletada com sucesso!")
        return super().delete(request, *args, **kwargs)

