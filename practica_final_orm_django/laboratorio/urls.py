from django.contrib import admin
from django.urls import path
from laboratorio.views import index,insertar_lab,mostrar_lab,editar_lab,actualizar_lab,eliminar_lab

urlpatterns = [
    path('', index, name='index'),
    path('insertar/', insertar_lab, name='insertar-lab'),
    path('mostrar/', mostrar_lab, name='mostrar-lab'),
    path('editar/<int:id>', editar_lab, name='editar-lab'),
    path('editar/actualizarlab/<int:id>',actualizar_lab, name='actualizar-lab'),
    path('eliminar/<int:id>', eliminar_lab, name='eliminar-lab'),
]