from rest_framework import viewsets
from .serializer import TareasSerializer
from .models import Tareas
# Create your views here.

#Creación del CRUD necesario.

class VistaTareas(viewsets.ModelViewSet):
    serializer_class = TareasSerializer
    queryset =  Tareas.objects.all()
