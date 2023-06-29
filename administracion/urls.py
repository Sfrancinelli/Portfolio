from django.urls import path
from administracion import views

urlpatterns = [

    path('', views.index_administracion, name='index_admin'),
    # path('orentacion/', views.orientacion_index, name='orientacion_index'),
    # path('orientacion/nuevo/', views.orientacion_nuevo, name='orientacion_nuevo'),
    # path('orientacion/editar/<int:id_orientacion>', views.orientacion_editar, name='orientacion_editar'),
    # path('orientacion/eliminar/<int:id_orientacion>', views.orientacion_eliminar, name='orientacion_eliminar'),
    # path('orientacion/buscar/', views.orientacion_buscar, name='buscar_orientaciones'),

]