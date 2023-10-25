from django import forms
from accounts.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Hasła nie pasują do siebie.")
        return confirm_password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.is_active = (
            True  # Ustawienie is_active na True, inaczej nie działa logowanie
        )
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
