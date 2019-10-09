from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Cardapio, Avaliacoes, Representante, Turma

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['data', 'tipo', 'descricao']

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ['disciplina','data', 'conteudo', 'tipo']

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = ['nome', 'turma']

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['nome']