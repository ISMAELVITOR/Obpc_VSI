# app/views/base_view.py
from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectedView(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'next'