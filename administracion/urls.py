from django.urls import path
from administracion import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index_administracion, name='index_admin'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/index.html'), name='logout'),
    # path('orentacion/', views.orientacion_index, name='orientacion_index'),
    # path('orientacion/nuevo/', views.orientacion_nuevo, name='orientacion_nuevo'),
    # path('orientacion/editar/<int:id_orientacion>', views.orientacion_editar, name='orientacion_editar'),
    # path('orientacion/eliminar/<int:id_orientacion>', views.orientacion_eliminar, name='orientacion_eliminar'),
    # path('orientacion/buscar/', views.orientacion_buscar, name='buscar_orientaciones'),
]
