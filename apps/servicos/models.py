from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    cliente = models.ForeignKey('clientes.Cliente', 
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='servicos')
    
    ativo = models.BooleanField(default=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome