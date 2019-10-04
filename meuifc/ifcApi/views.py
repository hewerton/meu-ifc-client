from django.shortcuts import render
from rest_framework import viewsets
from .models import Cardapio, Avaliacoes
from .serializers import CardapioSerializer, AvaliacoesSerializer

class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer