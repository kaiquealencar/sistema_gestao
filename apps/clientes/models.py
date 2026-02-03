from django.db import models
import re

from django.forms import ValidationError

class Cliente(models.Model):
    TIPO_CHOICES = (
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica"),
    )   
    
    tipo_cliente = models.CharField(max_length=5, choices=TIPO_CHOICES, default="PF")
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=False, null=False)

    email = models.EmailField(unique=True, blank=False, null=False)
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

    def clean(self):
        super().clean()

        if self.cpf_cnpj:
            self.cpf_cnpj = re.sub(r"\D", "", self.cpf_cnpj)
        if self.telefone:
            self.telefone = re.sub(r"\D", "", self.telefone)
        if self.cep:
            self.cep = re.sub(r"\D", "", self.cep)

        erros = {}

        if self.tipo_cliente == "PF" and (not self.cpf_cnpj or len(self.cpf_cnpj) != 11):
            erros['cpf_cnpj'] = "CPF deve ter 11 dígitos"
        if self.tipo_cliente == "PJ" and (not self.cpf_cnpj or len(self.cpf_cnpj) != 14):
            erros['cpf_cnpj'] = "CNPJ deve ter 14 dígitos"

        if self.telefone and len(self.telefone) not in [10, 11]:
            erros['telefone'] = "Telefone inválido"

        if self.cep and len(self.cep) != 8:
            erros['cep'] = "CEP inválido"

        if erros:
            raise ValidationError(erros)

    @property
    def telefone_formatado(self):
        if len(self.telefone) == 10:
            return f"({self.telefone[:2]}) {self.telefone[2:6]}-{self.telefone[6:]}"
        elif len(self.telefone) == 11:
            return f"({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:]}"
        return self.telefone

    @property
    def cep_formatado(self):
        if len(self.cep) == 8:
            return f"{self.cep[:5]}-{self.cep[5:]}"
        return self.cep
    
    @property
    def cpf_cnpj_formatado(self):
        if self.tipo_cliente == "PF" and len(self.cpf_cnpj) == 11:
            return f"{self.cpf_cnpj[:3]}.{self.cpf_cnpj[3:6]}.{self.cpf_cnpj[6:9]}-{self.cpf_cnpj[9:]}"
        elif self.tipo_cliente == "PJ" and len(self.cpf_cnpj) == 14:
            return f"{self.cpf_cnpj[:2]}.{self.cpf_cnpj[2:5]}.{self.cpf_cnpj[5:8]}/{self.cpf_cnpj[8:12]}-{self.cpf_cnpj[12:]}"
        return self.cpf_cnpj  
       
          


    def __str__(self):
        return self.nome