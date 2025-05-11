from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
