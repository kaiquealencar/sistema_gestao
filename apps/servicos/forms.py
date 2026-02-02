from django import forms
from common.forms import BaseForm
from .models import Servico 

class ServicoForm(BaseForm):
    class Meta:
        model = Servico
        fields = "nome", "descricao", "preco", "disponivel", "ativo"

        help_texts = {
            "nome": "Insira o nome do serviço.",
            "preco": "Defina o preço do serviço em Reais (R$).",
            "disponivel": "Marque se o serviço está disponível para contratação.",
        }

        labels = {
            "nome": "Nome do Serviço",
            "descricao": "Descrição",
            "preco": "Preço",
            "disponivel": "Disponível",
            "ativo": "Ativo",
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "disponivel": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }