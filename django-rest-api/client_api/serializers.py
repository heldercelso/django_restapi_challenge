from rest_framework import serializers 
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client

        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'cpf': {'write_only': True},
            'nome': {'write_only': True},
            'email': {'write_only': True},
            'dataDeNascimento': {'write_only': True},
            'sexo': {'write_only': True},
            'rendaMensal': {'write_only': True},
        }