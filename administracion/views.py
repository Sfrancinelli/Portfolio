from django.shortcuts import render, redirect
from administracion.forms import SignUpForm, LoginForm, NewPassForm, VerifyCodeForm, ForgotPass
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from projects.models import Project, Tag, ProjectTag, Category
from administracion.forms import ProyectoForm, EtiquetaForm, CategoriaForm
from django.core.files.storage import default_storage


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


# Proyectos
def proyectos_index(request):
    proyectos = Project.objects.all()
    return render(request, 'administracion/CRUD/Proyectos/index.html', {'proyectos': proyectos})


def proyectos_nuevo(request):
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyectos_index')
    else:
        formulario = ProyectoForm()
    return render(request, 'administracion/CRUD/Proyectos/new.html', {'form': formulario})


def proyectos_editar(request, id):
    try:
        proyecto = Project.objects.get(pk=id)
        previous_image_path = proyecto.image.path if proyecto.image else None
    except Project.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'GET':
        formulario = ProyectoForm(instance=proyecto)
        return render(request, 'administracion/CRUD/Proyectos/edit.html', {'form': formulario})

    elif request.method == 'POST':
        formulario = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if formulario.is_valid():

            proyecto = formulario.save(commit=False)

            if previous_image_path and default_storage.exists(previous_image_path):
                default_storage.delete(previous_image_path)

            proyecto.save()

            return redirect('proyectos_index')

    return render(request, 'administracion/CRUD/Proyectos/edit.html', {'form': formulario})


def proyectos_eliminar(request, id):
    try:
        proyecto = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    proyecto.image.storage.delete(proyecto.image.name)
    proyecto.delete()
    return redirect('proyectos_index')


def proyectos_buscar(request):
    nombre = request.GET.get('nombre')

    proyectos = Project.objects.filter(title__icontains=nombre)

    return render(request, 'administracion/CRUD/Proyectos/index.html', {'proyectos': proyectos})


# Etiquetas
def etiquetas_index(request):
    etiquetas = Tag.objects.all()
    return render(request, 'administracion/CRUD/Etiquetas/index.html', {'etiquetas': etiquetas})


def etiquetas_nuevo(request):
    if request.method == 'POST':
        formulario = EtiquetaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('etiquetas_index')
    else:
        formulario = EtiquetaForm()
    return render(request, 'administracion/CRUD/Etiquetas/new.html', {'form': formulario})


def etiquetas_editar(request, id):
    try:
        etiquetas = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'GET':
        formulario = EtiquetaForm(instance=etiquetas)
        return render(request, 'administracion/CRUD/Etiquetas/edit.html', {'form': formulario})

    elif request.method == 'POST':
        formulario = EtiquetaForm(request.POST, instance=etiquetas)
        if formulario.is_valid():

            formulario.save()

            return redirect('etiquetas_index')

    return render(request, 'administracion/CRUD/Etiquetas/edit.html', {'form': formulario})


def etiquetas_eliminar(request, id):
    try:
        etiquetas = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    etiquetas.delete()
    return redirect('etiquetas_index')


def etiquetas_buscar(request):
    nombre = request.GET.get('nombre')

    etiquetas = Tag.objects.filter(name__icontains=nombre)

    return render(request, 'administracion/CRUD/Etiquetas/index.html', {'etiquetas': etiquetas})


# Categorías
def categorias_index(request):
    categorias = Category.objects.all()
    return render(request, 'administracion/CRUD/Categorias/index.html', {'categorias': categorias})


def categorias_nuevo(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request, 'administracion/CRUD/Categorias/new.html', {'form': formulario})


def categorias_editar(request, id):
    try:
        categorias = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'GET':
        formulario = CategoriaForm(instance=categorias)
        return render(request, 'administracion/CRUD/Categorias/edit.html', {'form': formulario})

    elif request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=categorias)
        if formulario.is_valid():

            formulario.save()

            return redirect('categorias_index')

    return render(request, 'administracion/CRUD/Categorias/edit.html', {'form': formulario})


def categorias_eliminar(request, id):
    try:
        categorias = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    categorias.delete()
    return redirect('categorias_index')


def categorias_buscar(request):
    nombre = request.GET.get('nombre')

    categorias = Category.objects.filter(name__icontains=nombre)

    return render(request, 'administracion/CRUD/Categorias/index.html', {'categorias': categorias})
