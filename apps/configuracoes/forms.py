from django import forms
from common.forms import BaseForm
from .models import ConfiguracoesWhatsapp


class ConfiguracoesForm(BaseForm):
    class Meta:
        model = ConfiguracoesWhatsapp
        fields = "__all__"

        help_text = {
            "instancia": "Insira o nome da instância",
            "token": "Insira o token id do serviço",
            "client_token": "Insira o client token do serviço",
        }

        labels = {
            "instancia": "Nome da instância",
            "token": "Token Id",
            "client_token": "Client token",
        }

        widgets = {
            "instancia": forms.TextInput(attrs={"class": "form-control"}),
            "token": forms.PasswordInput(render_value=True, attrs={"class": "form-control"}),
            "client_token": forms.PasswordInput(render_value=True, attrs={"class": "form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
