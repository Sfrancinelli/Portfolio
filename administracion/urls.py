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

    path('categorias/', views.categorias_index, name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo, name='categorias_nuevo'),
    path('categorias/editar/<int:id>', views.categorias_editar, name='categorias_editar'),
    path('categorias/eliminar/<int:id>', views.categorias_eliminar, name='categorias_eliminar'),
    path('categorias/buscar/', views.categorias_buscar, name='categorias_buscar'),

    path('pro_tag/', views.pro_tag_index, name='pro_tag_index'),
    path('pro_tag/nuevo/', views.pro_tag_nuevo, name='pro_tag_nuevo'),
    path('pro_tag/editar/<int:id>', views.pro_tag_editar, name='pro_tag_editar'),
    path('pro_tag/eliminar/<int:id>', views.pro_tag_eliminar, name='pro_tag_eliminar'),
    path('pro_tag/buscar/', views.pro_tag_buscar, name='pro_tag_buscar'),
]
