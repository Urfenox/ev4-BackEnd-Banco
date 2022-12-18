from rest_framework import serializers
from .models import Accionista

class AccionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accionista
        fields = '__all__'
