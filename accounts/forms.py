from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Account


"""Vous gere l'authentification

    il vous gere la logique de l'authentification avec des formes deja predifinis et customisable

"""


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _("This account is inactive."),
                code="inactive",
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control mb-3", "required": True, "placeholder": "Email Adress"})

        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-3", "required": True, "placeholder": "Password"})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "required": True, "placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "required": True, "placeholder": "Example@email.com"})
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "required": True, "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "required": True, "placeholder": "Confirm Password"})


