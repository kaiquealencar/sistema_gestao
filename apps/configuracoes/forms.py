from django import forms
from common.forms import BaseForm
from .models import ConfiguracoesWhatsapp


class ConfiguracoesForm(BaseForm):
    class Meta:
        model = ConfiguracoesWhatsapp
        fields = "__all__"

        help_text = {
            "nome_instancia": "Insira o nome da instância",
            "instancia_id": "Insira o ID da instância",
            "token": "Insira o token id do serviço",
            "client_token": "Insira o client token do serviço",
        }

        labels = {
            "nome_instancia": "Nome da instância",
            "instancia_id": "Instância ID",
            "token": "Token Id",
            "client_token": "Client token",
        }

        widgets = {
            "nome_instancia": forms.TextInput(attrs={"class": "form-control"}),
            "instancia_id": forms.PasswordInput(render_value=True, attrs={"class": "form-control"}),
            "token": forms.PasswordInput(render_value=True, attrs={"class": "form-control"}),
            "client_token": forms.PasswordInput(render_value=True, attrs={"class": "form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
