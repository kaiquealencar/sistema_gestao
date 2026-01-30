from django import forms
import re
from common.forms import BaseForm
from .models import Cliente
from .validators import validar_cpf_cnpj

class ClienteForm(BaseForm):
    class Meta:        
        model = Cliente
        fields = "__all__"

        
        labels = {
            "tipo_cliente": "Tipo de Cliente",
            "nome": "Nome Completo",
            "cpf_cnpj": "CPF/CNPJ",
            "data_nascimento": "Data de Nascimento",
            "email": "E-mail",
            "telefone": "Telefone",
            "endereco": "Endereço",
            "cep": "CEP",
            "logradouro": "Logradouro",
            "bairro": "Bairro",
            "cidade": "Cidade",
            "estado": "UF",
            "numero": "Número",
        }

        widgets = {
            "cep": forms.TextInput({"id": "cep"}), 
            "logradouro": forms.TextInput({"id": "logradouro", "class": "form-control campo-auto", "readonly": "true"}),
            "bairro": forms.TextInput({"id": "bairro", "class": "form-control campo-auto", "readonly": "true"}),    
            "cidade": forms.TextInput({"id": "cidade", "class": "form-control campo-auto", "readonly": "true"}),
            "estado": forms.TextInput({"id": "estado", "class": "form-control campo-auto", "readonly": "true"}),
            "numero": forms.TextInput({"id": "numero"}),
            "tipo_cliente": forms.Select({"id": "tipo_cliente", "class": "form-select"}),
            "telefone": forms.TextInput(attrs={"id": "telefone", "class": "form-control"}),
            "cpf": forms.TextInput(attrs={"id": "cpf", "class": "form-control"}),
            "cnpj": forms.TextInput(attrs={"id": "cnpj", "class": "form-control"}),
            
        }
                


        help_texts = {
            "cpf": "Digite o CPF sem pontos ou traços.",
            "data_nascimento": "Formato: DD/MM/AAAA",
            "telefone": "Formato: (XX) XXXXX-XXXX",             
        }

    def clean_cpf_cnpj(self):
        valor = self.cleaned_data['cpf_cnpj']

        try:
            validar_cpf_cnpj(valor)
        except ValueError as e:
            raise forms.ValidationError(str(e))
        return valor

