from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage:index')
    template_name = 'users/signup.html'


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('homepage:index')
