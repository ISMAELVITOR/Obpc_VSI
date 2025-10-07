# app/views/auth_views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from app.forms.login_form import LoginForm
from app.forms.pessoa_form import PessoaRegisterForm
from app.models.pessoa import Pessoa

class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class RegisterView(CreateView):
    model = Pessoa
    form_class = PessoaRegisterForm
    template_name = "auth/register.html"   
    success_url = reverse_lazy("login")



