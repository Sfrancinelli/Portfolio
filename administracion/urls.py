from django.urls import path
from administracion import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index_administracion, name='index_admin'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/index.html'), name='logout'),
    path('profile/', views.profile, name='profile'),


    path('proyectos/', views.proyectos_index, name='proyectos_index'),
    path('proyectos/nuevo/', views.proyectos_nuevo, name='proyectos_nuevo'),
    path('proyectos/editar/<int:id>', views.proyectos_editar, name='proyectos_editar'),
    path('proyectos/eliminar/<int:id>', views.proyectos_eliminar, name='proyectos_eliminar'),
    path('proyectos/buscar/', views.proyectos_buscar, name='proyectos_buscar'),
]
