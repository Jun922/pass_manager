from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


class LoginView(TemplateView):
    template_name = "accounts/login.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("pw_recorder:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response
