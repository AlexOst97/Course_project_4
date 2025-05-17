from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "avatar",
            "phone_number",
            "country",
        ]


class ManagerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "is_active",
        ]
