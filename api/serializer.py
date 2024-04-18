from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        #fields=('codigo','nombre','apellido','email','fechaNacimiento','pago')
        fields='__all__'