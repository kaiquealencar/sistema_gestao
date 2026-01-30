from django.db import models

class Cliente(models.Model):
    TIPO_CHOICES = (
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica"),
    )

    tipo_cliente = models.CharField(max_length=5, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20, unique=True)

    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)

    observacoes = models.TextField(blank=True, null=True)

    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome