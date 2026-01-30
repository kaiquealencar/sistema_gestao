from django import forms
from common.forms import BaseForm
from .models import Cliente

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
        }


        help_texts = {
            "cpf": "Digite o CPF sem pontos ou traços.",
            "data_nascimento": "Formato: DD/MM/AAAA",
            "telefone": "Formato: (XX) XXXXX-XXXX",             
        }
