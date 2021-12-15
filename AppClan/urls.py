from django.urls import path
from AppClan import views

urlpatterns = [
    
    path('', views.inicio, name = "Inicio"),
    path('/integrantes', views.integrantes, name = "Integrantes"),
    path('/integranteFormulario', views.integranteFormulario, name="IntegranteFormulario"),
    path('/vehiculos', views.vehiculos, name = "Vehiculos"),
    path('/vehiculoFormulario', views.vehiculoFormulario, name="VehiculoFormulario"),
    path('/comentarios', views.comentarios, name = "Comentarios"),
    path('/comentarioFormulario', views.comentarioFormulario, name="ComentarioFormulario"),    
]