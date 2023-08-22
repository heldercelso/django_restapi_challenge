from rest_framework import serializers 
from .models import Plans


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'


class PlansPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'nome': {'write_only': True},
            'susep': {'write_only': True},
            'expiracaoDeVenda': {'write_only': True},
            'valorMinimoAporteInicial': {'write_only': True},
            'valorMinimoAporteExtra': {'write_only': True},
            'idadeDeEntrada': {'write_only': True},
            'idadeDeSaida': {'write_only': True},
            'carenciaInicialDeResgate': {'write_only': True},
            'carenciaEntreResgates': {'write_only': True},
        }