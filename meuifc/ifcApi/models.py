from django.db import models

class Cardapio(models.Model):
    data = models.CharField(max_length=50)

    refeicoes = (
        ('CM','Café da Manhã'),
        ('AL','Almoço'),
        ('LC','Lanche da Tarde'),
        ('JT','Janta')
    )

    tipo = models.CharField(max_length=1, choices=refeicoes)

    descricao = models.CharField(max_length=500)

    #def __str__(self):
     #  return self.nome

class Avaliacoes(models.Model):
    disciplina = models.CharField(max_length=100)

    data = models.CharField(max_length=50)

    conteudo = models.CharField(max_length=350)

    avaliacoes_choice = (
        ('PV', 'Prova'),
        ('TP', 'Trabalho Prático'),
        ('SM', 'Seminário')
    )

    tipo = models.CharField(max_length=1, choices=avaliacoes_choice)