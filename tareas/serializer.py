from rest_framework import serializers
from .models import Tareas


class TareasSerializer(serializers.ModelSerializer):
    class Meta:

        model = Tareas
        fields = ('id', 'titulo', 'descripcion', 'done')

        #cuando se tienen muchos campos para serializar se opta por:
        # fields = '__all__'
