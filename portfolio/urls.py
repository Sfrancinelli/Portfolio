"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views as p_views
from administracion import views as a_views
from administracion.admin import my_admin

urlpatterns = [
    path('admin_og/', admin.site.urls),
    path('admin/', my_admin.urls),
    path('', p_views.index, name='index'),
    path('projects/<int:id>/', p_views.projects),
    path('about/', p_views.about, name='about'),
    path('contact/', p_views.contact, name='contact'),
    path('administracion/', include('administracion.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
