from common.forms import BaseForm
from .models import Cliente

class ClienteForm(BaseForm):
    class Meta:
        model = Cliente
        fields = "__all__"

        labels = {
            "nome": "Nome Completo",
            "cpf": "CPF",
            "data_nascimento": "Data de Nascimento",
            "email": "E-mail",
            "telefone": "Telefone",
            "endereco": "Endereço",
        }

        help_texts = {
            "cpf": "Digite o CPF sem pontos ou traços.",
            "data_nascimento": "Formato: DD/MM/AAAA",
            "telefone": "Formato: (XX) XXXXX-XXXX",             
        }