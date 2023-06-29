from django.shortcuts import render


# Create your views here.
def index_administracion(request):
    return render(request, 'administracion/index.html')
