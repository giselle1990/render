from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verificar/', views.verificar_supresion_de_datos, name='verificar_supresion_de_datos'),
    path('historial/', views.historial, name='historial'),
    path('datos/', views.datos_view, name='datos_view'),
]
