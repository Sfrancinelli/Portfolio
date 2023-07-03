from django.shortcuts import render, redirect
from administracion.forms import SignUpForm, LoginForm, NewPassForm, VerifyCodeForm, ForgotPass
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index_administracion(request):
    return render(request, 'administracion/index.html')


def login(request):
    if request.methos == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido/a {username}')
                return redirect('index')
            else:
                messages.error(request, 'Las credenciales ingresadas no son correctas')
                context = {'form': form}
                return render(request, 'administracion/authentication-login.html', context)
        else:
            messages.error(request, 'Por favor introduzca datos válidos')
            context = {'form': form}
            return render(request, 'administracion/authentication-login.html', context)
    else:
        context = {'form': LoginForm()}
        return render(request, 'administracion/authentication-login.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registro exitoso')
            context = {'form': form}
            return render(request, 'administracion/authentication-login.html', context)
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            context = {'form': form}
            return render(request, 'administracion/authentication-register.html', context)
    else:
        context = {'form': SignUpForm()}
        return render(request, 'administracion/authentication-register.html', context)
