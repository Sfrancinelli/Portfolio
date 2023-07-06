from django.shortcuts import render, redirect
from administracion.forms import SignUpForm, LoginForm, NewPassForm, VerifyCodeForm, ForgotPass
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from projects.models import Project
from administracion.forms import ProyectoForm


# Create your views here.
def index_administracion(request):
    return render(request, 'administracion/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
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


def profile(request):
    return HttpResponse('Perfil')


def proyectos_index(request):
    proyectos = Project.objects.all()
    return render(request, 'administracion/CRUD/Proyectos/index.html', {'proyectos': proyectos})


def proyectos_nuevo(request):
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyectos_index')
    else:
        formulario = ProyectoForm()
    return render(request, 'administracion/CRUD/Proyectos/new.html', {'form': formulario})
