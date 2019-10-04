from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Cardapio, Avaliacoes

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['data', 'tipo', 'descricao']

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ['disciplina','data', 'conteudo', 'tipo']