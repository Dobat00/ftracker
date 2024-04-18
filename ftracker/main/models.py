from django.db import models

# Create your models here.


class Gasto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()

    def __str__(self):
        return self.nome
