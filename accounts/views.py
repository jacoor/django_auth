from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy(
        ""
    )  # Przekierowanie po udanej rejestracji. Tak, puste. Ćwiczenie dla Was.

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return valid
