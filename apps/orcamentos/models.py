from django.db import models
from django.utils import timezone

class Orcamento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),   
        ("cancelado", "Cancelado"),
    ]
    
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    servicos = models.ManyToManyField("servicos.Servico", through="ItemOrcamento")
    data_criacao = models.DateTimeField(default=timezone.now)
    validade = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")
    observacoes = models.TextField(blank=True, null=True)


    @property
    def total(self):
        total = sum(item.subtotal for item in self.itemorcamento_set.all())
        return total
    
    def __str__(self):
        return f"Orçamento #{self.id} - {self.cliente.nome} - {self.status}"
    
class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    servico = models.ForeignKey("servicos.Servico", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  

    @property
    def subtotal(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f'{self.servico.nome} x {self.quantidade}'
    


