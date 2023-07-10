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

    path('etiquetas/', views.etiquetas_index, name='etiquetas_index'),
    path('etiquetas/nuevo/', views.etiquetas_nuevo, name='etiquetas_nuevo'),
    path('etiquetas/editar/<int:id>', views.etiquetas_editar, name='etiquetas_editar'),
    path('etiquetas/eliminar/<int:id>', views.etiquetas_eliminar, name='etiquetas_eliminar'),
    path('etiquetas/buscar/', views.etiquetas_buscar, name='etiquetas_buscar'),
]
