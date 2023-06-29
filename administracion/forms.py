from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'user',
                'class': 'form-control',
                'placeholder': 'Usuario',
                'minlength': '8',
                'requred': 'True',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True,
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'title': 'Por favor, ingrese un correo electrónico válido (ejemplo@dominio.com)'
            }
        )
    )

    password1= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password1',
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass',
                'class': 'form-control',
                'placeholder': 'Repetir contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    def clean_password1(self):
        password1 = self.cleaned_data['password']

        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not any(c.isupper() for c in password1):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
        if not any(c.islower() for c in password1):
            raise ValidationError('La contraseña debe tener al menos una letra minúscula')
        if not any(c.isdigit() for c in password1):
            raise ValidationError('La contraseña debe tener al menos un número')
        return password1
    
    def clean_password2(self):
        password2 = self.cleaned_data['password']
        if len(password2) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not any(c.isupper() for c in password2):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
        if not any(c.islower() for c in password2):
            raise ValidationError('La contraseña debe tener al menos una letra minúscula')
        if not any(c.isdigit() for c in password2):
            raise ValidationError('La contraseña debe tener al menos un número')
        return password2
    
    def clean_email(self, value):
        email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if not re.match(email_regex, value):
            raise ValidationError('Correo electrónico inválido.')