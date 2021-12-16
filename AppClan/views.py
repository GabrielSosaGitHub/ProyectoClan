from django.shortcuts import render

from .forms import *

from .models import *

# Create your views here.
def inicio(request):
    return render(request, "AppClan/inicio.html")

def integrantes(request):
    return render(request, "AppClan/integrantes.html")

def vehiculos(request):
    return render(request, "AppClan/vehiculos.html")

def comentarios(request):
    return render(request, "AppClan/comentarios.html")

def integranteFormulario(request):

    if request.method == 'POST':

        miFormulario = IntegranteFormulario(request.POST)

        if miFormulario.is_valid(): # Validación de Django !!

            informacion = miFormulario.cleaned_data

            integrante = Integrante(
                
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                fechaDeNacimiento=informacion['fechaDeNacimiento'],
                esMascota=informacion['esMascota'])
        
            integrante.save() # Este save es el que guarda en la base de datos.
        
        return render(request, 'AppClan/cargaIntegranteExitosa.html')

    else:

        miFormulario = IntegranteFormulario()

    return render(request, 'AppClan/integranteFormulario.html', {"miFormulario":miFormulario})

def cargaIntegranteExitosa(request):
    return render(request, "AppClan/cargaIntegranteExitosa.html")

def busquedaIntegrante(request):

    return render(request, 'AppClan/busquedaIntegrante.html')

def resultadoBusquedaIntegrante(request):
    
    return render(request, "AppClan/resultadoBusquedaIntegrante.html")

def buscarIntegrante(request):
      
    if request.GET["apellido"]:
        
        apellido = request.GET["apellido"]
        
        # nombres = Integrante.objects.filter(apellido__icontains=apellido)
        nombres = Integrante.objects.filter(apellido=apellido)
               
        respuesta = f"ESTOY BUSCANDO A: {request.GET['apellido']}"
        
        return render(request, "AppClan/resultadoBusquedaIntegrante.html",{"nombres":nombres, "apellido":apellido})
         
    else: 
        
        respuesta = "Pasame el apellido, porfa"     
    
    return HttpResponse(respuesta)


def vehiculoFormulario(request):

    if request.method == 'POST':

        miFormulario = VehiculoFormulario(request.POST)

        if miFormulario.is_valid(): # Validación de Django !!

            informacion = miFormulario.cleaned_data

            vehiculo = Vehiculo(
                
                marca=informacion['marca'],
                nombre=informacion['nombre'],
                modelo=informacion['modelo'],
                esEcofriendly=informacion['esEcofriendly'])
        
            vehiculo.save() # Este save es el que guarda en la base de datos.
        
        return render(request, 'AppClan/cargaVehiculoExitosa.html')

    else:

        miFormulario = VehiculoFormulario()

    return render(request, 'AppClan/vehiculoFormulario.html', {"miFormulario":miFormulario})

def cargaVehiculoExitosa(request):
    return render(request, "AppClan/cargaVehiculoExitosa.html")

def comentarioFormulario(request):

    if request.method == 'POST':

        miFormulario = ComentarioFormulario(request.POST)

        if miFormulario.is_valid(): # Validación de Django !!

            informacion = miFormulario.cleaned_data

            comentario = Comentario(
                
                nombreComentarista=informacion['nombreComentarista'],
                email=informacion['email'],
                texto=informacion['texto'])
        
            comentario.save() # Este save es el que guarda en la base de datos.
        
        return render(request, 'AppClan/cargaComentarioExitosa.html')

    else:

        miFormulario = ComentarioFormulario()

    return render(request, 'AppClan/comentarioFormulario.html', {"miFormulario":miFormulario})

def cargaComentarioExitosa(request):
    return render(request, "AppClan/cargaComentarioExitosa.html")

