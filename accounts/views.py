from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("home")  # Przekierowanie po udanej rejestracji

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
