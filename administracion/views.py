from django.shortcuts import render


# Create your views here.
def index_administracion(request):
    return render(request, 'administracion/index.html')


def login(request):
    return render(request, 'administracion/authentication-login.html')


def register(request):
    return render(request, 'administracion/authentication-register.html')
