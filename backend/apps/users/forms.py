from django import forms

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "email", "password", "first_name", "last_name",)

        widgets = {
            "password": forms.PasswordInput(),
        }
