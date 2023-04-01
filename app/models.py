from django.db import models

class Cliente(models.Model):
    Nome = models.CharField(max_length=100)
    Cpf = models.IntegerField(max_length=11)
    Email = models.CharField(max_length=40)
    Contato = models.IntegerField(max_length=40)

    def __str__(self):
        return self.Nome
        
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome