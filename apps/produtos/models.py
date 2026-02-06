import random
import string

from django.db import models

class Produtos(models.Model):
    nome = models.CharField("Nome do Produto", max_length=300)
    descricao = models.TextField("Descrição", blank=True, null=True)
    categoria = models.CharField("Categoria", blank=True, null=True)
    codigo = models.CharField("Código Produto", max_length=20, unique=True, blank=True)

    preco_custo = models.DecimalField("Preço de Custo", max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField("Preço de Venda", max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade_estoque = models.PositiveIntegerField("Quantidade de Estoque", default=0)
    estoque_minimo = models.PositiveBigIntegerField("Estoque Mínimo", default=0)
    unidade_medida = models.CharField("Unidade de Medida", max_length=20, default="un")

    fornecedor = models.CharField("Fornecedor", max_length=100, blank=True, null=True)
    imagem = models.ImageField("Imagem do Produto", upload_to="protudos/", blank=True, null=True)
    codigo_barras = models.CharField("Código de Barras", max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.cdigo})"
    
    def save(self, *args, **kwargs):

        if not self.codigo:
            iniciais_categoria = ''.join([c[0] for c in (self.categoria or "").split()]).upper()
            iniciais_nome = ''.join([c[0] for c in self.nome.split()]).upper()
            codigo = ''.join(random.choices(string.digits, k=3))

            self.codigo = f"{iniciais_categoria}{iniciais_nome}{codigo}"

            while Produtos.objects.filter(codigo=self.codigo).exists():
                codigo =  ''.join(random.choices(string.digits, k=3))
                self.sku = f"{iniciais_categoria}-{iniciais_nome}-{codigo}"

        super().save(*args, **kwargs)