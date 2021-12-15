from django import forms

class IntegranteFormulario(forms.Form): # EstadioFormulario hereda de forms.Form

    # Campos que queremos que se vean en la web.
    nombre = forms.CharField()
    apellido = forms.CharField()
    fechaDeNacimiento = forms.DateField()
    esMascota = forms.BooleanField()

class VehiculoFormulario(forms.Form):

    # Campos que queremos que se vean en la web.
    marca = forms.CharField()
    nombre = forms.CharField()
    modelo = forms.IntegerField()
    esEcofriendly = forms.BooleanField()
    
class ComentarioFormulario(forms.Form):

    # Campos que queremos que se vean en la web.
    nombreComentarista = forms.CharField()
    email = forms.EmailField()
    texto = forms.CharField()

