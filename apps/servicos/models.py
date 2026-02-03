from django.db import models
from django.core.exceptions import ValidationError

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    
    ativo = models.BooleanField(default=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.preco < 0:
            raise ValidationError("O preço não pode ser negativo.")


    def __str__(self):
        return self.nome