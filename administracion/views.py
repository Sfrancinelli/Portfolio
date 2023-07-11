from django.shortcuts import render, redirect, get_object_or_404
from administracion.forms import SignUpForm, LoginForm, NewPassForm, VerifyCodeForm, ForgotPass
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from projects.models import Project, Tag, ProjectTag, Category
from administracion.forms import ProyectoForm, EtiquetaForm, CategoriaForm, ProjectTagForm
from django.core.files.storage import default_storage
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test


def staff_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda user: user.is_staff)(view_func))
    return decorated_view_func


# Create your views here.
@staff_required
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
@staff_required
def proyectos_index(request):
    proyectos = Project.objects.all()
    return render(request, 'administracion/CRUD/Proyectos/index.html', {'proyectos': proyectos})


@staff_required
def proyectos_nuevo(request):
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyectos_index')
    else:
        formulario = ProyectoForm()
    return render(request, 'administracion/CRUD/Proyectos/new.html', {'form': formulario})


@staff_required
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


@staff_required
def proyectos_eliminar(request, id):
    try:
        proyecto = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    proyecto.image.storage.delete(proyecto.image.name)
    proyecto.delete()
    return redirect('proyectos_index')


@staff_required
def proyectos_buscar(request):
    nombre = request.GET.get('nombre')

    proyectos = Project.objects.filter(title__icontains=nombre)

    return render(request, 'administracion/CRUD/Proyectos/index.html', {'proyectos': proyectos})


# Etiquetas
@staff_required
def etiquetas_index(request):
    etiquetas = Tag.objects.all()
    return render(request, 'administracion/CRUD/Etiquetas/index.html', {'etiquetas': etiquetas})


@staff_required
def etiquetas_nuevo(request):
    if request.method == 'POST':
        formulario = EtiquetaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('etiquetas_index')
    else:
        formulario = EtiquetaForm()
    return render(request, 'administracion/CRUD/Etiquetas/new.html', {'form': formulario})


@staff_required
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


@staff_required
def etiquetas_eliminar(request, id):
    try:
        etiquetas = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    etiquetas.delete()
    return redirect('etiquetas_index')


@staff_required
def etiquetas_buscar(request):
    nombre = request.GET.get('nombre')

    etiquetas = Tag.objects.filter(name__icontains=nombre)

    return render(request, 'administracion/CRUD/Etiquetas/index.html', {'etiquetas': etiquetas})


# Categorías
@staff_required
def categorias_index(request):
    categorias = Category.objects.all()
    return render(request, 'administracion/CRUD/Categorias/index.html', {'categorias': categorias})


@staff_required
def categorias_nuevo(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request, 'administracion/CRUD/Categorias/new.html', {'form': formulario})


@staff_required
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


@staff_required
def categorias_eliminar(request, id):
    try:
        categorias = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    categorias.delete()
    return redirect('categorias_index')


@staff_required
def categorias_buscar(request):
    nombre = request.GET.get('nombre')

    categorias = Category.objects.filter(name__icontains=nombre)

    return render(request, 'administracion/CRUD/Categorias/index.html', {'categorias': categorias})


# Proyecto-Etiquetas
@staff_required
def pro_tag_index(request):
    pro_tags = ProjectTag.objects.all()
    return render(request, 'administracion/CRUD/Eti-Pro/index.html', {'pro_tags': pro_tags})


@staff_required
def pro_tag_nuevo(request):
    if request.method == 'POST':
        formulario = ProjectTagForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('pro_tag_index')
    else:
        formulario = ProjectTagForm()
    return render(request, 'administracion/CRUD/Eti-Pro/new.html', {'form': formulario})


@staff_required
def pro_tag_editar(request, id):
    try:
        pro_tags = ProjectTag.objects.get(pk=id)
    except ProjectTag.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'GET':
        formulario = ProjectTagForm(instance=pro_tags)
        return render(request, 'administracion/CRUD/Eti-Pro/edit.html', {'form': formulario})

    elif request.method == 'POST':
        formulario = ProjectTagForm(request.POST, instance=pro_tags)
        if formulario.is_valid():

            formulario.save()

            return redirect('pro_tag_index')

    return render(request, 'administracion/CRUD/Eti-Pro/edit.html', {'form': formulario})


@staff_required
def pro_tag_eliminar(request, id):
    try:
        pro_tags = ProjectTag.objects.get(pk=id)
    except ProjectTag.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    pro_tags.delete()
    return redirect('pro_tag_index')


@staff_required
def pro_tag_buscar(request):
    nombre = request.GET.get('nombre')

    pro_tags = ProjectTag.objects.filter(
        Q(project__title__icontains=nombre) | Q(tag__name__icontains=nombre)
    )

    return render(request, 'administracion/CRUD/Eti-Pro/index.html', {'pro_tags': pro_tags})


@login_required
def give_staff(request, user_id):

    user = get_object_or_404(User, id=user_id)
    user.is_superuser = True
    user.save()

    messages.success(request, 'Permiso de super-user obtenido.')
    return redirect('index')
