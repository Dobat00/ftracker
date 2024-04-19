from django.db import models

# Create your models here.


class Gasto(models.Model):
    categoria_lista = [
        ('Contas do mes', 'Contas do mes'),
        ('Lazer', 'Lazer'),
        ('Compras', "Compras"),
    ]
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    categoria = models.CharField(max_length=200, choices=categoria_lista, null=True)

    def __str__(self):
        return self.nome
