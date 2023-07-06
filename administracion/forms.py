from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from projects.models import Project, Category, ProjectTag, Tag


def validate_pass(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres')
    if not any(c.isupper() for c in value):
        raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
    if not any(c.islower() for c in value):
        raise ValidationError('La contraseña debe tener al menos una letra minúscula')
    if not any(c.isdigit() for c in value):
        raise ValidationError('La contraseña debe tener al menos un número')
    return value


def check_email(value):
    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido.')


class LoginForm(forms.Form):
    user = forms.CharField(
        min_length=8,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario',
            'id': 'exampleInputEmail1'
        }),
        label=False
    )
    password = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'exampleInputPassword1',
            'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
            'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.'
        }),
        label=False
    )


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'exampleInputtext1',
                'class': 'form-control',
                'placeholder': 'Usuario',
                'minlength': '8',
                'requred': 'True',
            }
        )
    )

    email = forms.EmailField(
        validators=(check_email,),
        widget=forms.EmailInput(
            attrs={
                'id': 'exampleInputEmail1',
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True,
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'title': 'Por favor, ingrese un correo electrónico válido (ejemplo@dominio.com)'
            }
        )
    )

    password1 = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'exampleInputPassword1',
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    password2 = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'exampleInputPassword2',
                'class': 'form-control',
                'placeholder': 'Repetir contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )


class ForgotPass(forms.Form):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'forgot_user',
                'class': 'forgot_input',
                'placeholder': 'Usuario',
                'minlength': '8',
                'required': True,
            }
        )
    )

    email = forms.EmailField(
        validators=(check_email,),
        widget=forms.EmailInput(
            attrs={
                'id': 'forgot_email',
                'class': 'forgot_input',
                'placeholder': 'Email de recuperación',
                'required': True,
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'title': 'Por favor, ingrese un correo electrónico válido (ejemplo@dominio.com)',
            }
        )
    )


class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'id': 'code',
                'class': 'forgot_input',
                'placeholder': 'Código',
                'required': True,
            }
        )
    )


class NewPassForm(forms.Form):
    new_pass = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass',
                'class': 'forgot_input',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    pass_confirm = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass_confirm',
                'class': 'forgot_input',
                'placeholder': 'Repetir contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        new_pass = cleaned_data.get('new_pass')
        pass_confirm = cleaned_data.get('pass_confirm')

        if new_pass and pass_confirm and new_pass != pass_confirm:
            self.add_error('new_pass', 'Las contraseñas no coinciden.')
            self.add_error('pass_confirm', 'Las contraseñas no coinciden.')
            raise ValidationError("Las contraseñas no coinciden")


class ProyectoForm(forms.ModelForm):
    
    class Meta:
        model = Project

        fields = ['title', 'description', 'image', 'categories']

    title = forms.CharField(
        label='Title',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label='Descripción',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(
        label='Imágen representativa',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        label='Categorías (CTRL + click para selección múltiple)'
    )
