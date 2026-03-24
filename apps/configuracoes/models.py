from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from cryptography.fernet import Fernet
import base64
import hashlib


def get_fernet():
    key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))


class EncryptedField(models.TextField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            return get_fernet().decrypt(value.encode()).decode()
        except Exception:
            return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return get_fernet().encrypt(value.encode()).decode()


class ConfiguracoesWhatsapp(models.Model):
    nome_instancia = models.CharField(max_length=100, default="")
    instancia_id = EncryptedField(default="")
    token = EncryptedField()
    client_token = EncryptedField(null=True, blank=True)
    url_base = models.URLField(max_length=2000)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuração API Whatsapp"
        verbose_name_plural = "Configurações API Whatsapp"
        constraints = [
            models.UniqueConstraint(
                fields=["ativo"],
                condition=models.Q(ativo=True),
                name="unique_config_whatsapp_ativa"
            )
        ]

    def clean(self):
        if self.ativo:
            qs = ConfiguracoesWhatsapp.objects.filter(ativo=True)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError("Já existe uma configuração WhatsApp ativa.")

    def __str__(self):
        return f"Whatsapp {self.nome_instancia}"