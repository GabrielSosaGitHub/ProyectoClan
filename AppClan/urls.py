from django.urls import path
from AppClan import views

urlpatterns = [
    
    path('', views.inicio, name = "Inicio"),
    path('/integrantes', views.integrantes, name = "Integrantes"),
    path('/integranteFormulario', views.integranteFormulario, name="IntegranteFormulario"),
    path('/cargaIntegranteExitosa', views.cargaIntegranteExitosa, name = "CargaIntegranteExitosa"),
    path('/busquedaIntegrante', views.busquedaIntegrante, name = "BusquedaIntegrante"),
    path('/resultadoBusquedaIntegrante', views.resultadoBusquedaIntegrante, name = "ResultadoBusquedaIntegrante"),
    path('/buscarIntegrante', views.buscarIntegrante, name = "BuscarIntegrante"),
    path('/vehiculos', views.vehiculos, name = "Vehiculos"),
    path('/vehiculoFormulario', views.vehiculoFormulario, name="VehiculoFormulario"),
    path('/cargaVehiculoExitosa', views.cargaVehiculoExitosa, name = "CargaVehiculoExitosa"),
    path('/busquedaVehiculo', views.busquedaVehiculo, name = "BusquedaVehiculo"),
    path('/resultadoBusquedaVehiculo', views.resultadoBusquedaVehiculo, name = "ResultadoBusquedaVehiculo"),
    path('/buscarVehiculo', views.buscarVehiculo, name = "BuscarVehiculo"),
    path('/comentarios', views.comentarios, name = "Comentarios"),
    path('/comentarioFormulario', views.comentarioFormulario, name="ComentarioFormulario"), 
    path('/cargaComentarioExitosa', views.cargaComentarioExitosa, name = "CargaComentarioExitosa"),   
]