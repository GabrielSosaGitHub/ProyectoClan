from django.db import models

# Create your models here.
class Integrante(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    fechaDeNacimiento = models.DateField()
    esMascota = models.BooleanField()
    
    def __str__(self):
        return f"// Nombre: {self.nombre} // Apellido: {self.apellido} // Fecha de nacimiento: {self.fechaDeNacimiento} // Es mascota: {self.esMascota} //"
    
class Vehiculo(models.Model):
    
    marca = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    modelo = models.IntegerField()
    esEcofriendly = models.BooleanField()
    
    def __str__(self):
        return f"// Marca: {self.marca} // Nombre: {self.nombre} // Modelo: {self.modelo} // Es ecofriendly: {self.esEcofriendly} //"
    
class Comentario(models.Model):
    
    nombreComentarista = models.CharField(max_length=30)
    email = models.EmailField()
    texto = models.CharField(max_length=200)
    
    def __str__(self):
        return f"// Nombre de comentarista: {self.nombreComentarista} // Email: {self.email} // Comentario: {self.texto[:20]}... //"
