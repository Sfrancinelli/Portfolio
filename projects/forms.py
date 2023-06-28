from django import forms
from django.core.exceptions import ValidationError
from projects.models import Contact
import re


def validate_nombres(value):
    if len(value) < 4:
        raise ValidationError('El nombre debe tener al menos 4 caracteres')
    if len(value) > 155:
        raise ValidationError('El nombre no puede tener más de 155 caracteres')
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError('El nombre solo debe contener letras y espacios')


def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Ingrese un correo electrónico válido (ejemplo@dominio.com)')
    return value


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'company', 'email', 'message']

    name = forms.CharField(
        label='Nombre',
        required=True,
        error_messages={'required': 'El nombre no puede quedar vacío'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'name': 'nombres',
            'required': True,
            'placeholder': 'Nombre/s'
        }),
        validators=[validate_nombres]
    )

    company = forms.CharField(
        label='Empresa',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'company',
            'name': 'company',
            'required': False,
            'placeholder': 'Tu empresa'
        })
    )

    email = forms.EmailField(
        label='Email',
        error_messages={'required': 'El email no puede quedar vacío'},
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'required': True,
            'placeholder': 'ejemplo@gmail.com',
            'name': 'email'
        }),
        validators=[validate_email]
    )

    message = forms.CharField(
        label='Mensaje',
        max_length=800,
        error_messages={'required': 'El mensaje de contacto no puede quedar vacío'},
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Mensaje de contacto',
            'name': 'message',
            'id': 'message',
            'required': True,
            'rows': 3,
        })
    )
