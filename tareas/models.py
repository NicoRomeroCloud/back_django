from django.db import models

# Create your models here.

class Tareas(models.Model):

    # CharField es para decir que será un texto(String)
    titulo = models.CharField(max_length=200)

    # TextField ya que la descripción suele ser más extensa que unos simples caracteres.
    descripcion = models.TextField(blank=True)

    # Propiedad boleana
    done = models.BooleanField(default=False)
    
    # Para crear el espacio de codigo de esta nueva tabla de inserta en la terminal: python manage.py makemigrations (tareas); para solo realizar las migraciones de esa carpeta.

    # Para mostrar titulo de la tarea en elpanel de admin.
    def __str__(self):
        return self.titulo
    