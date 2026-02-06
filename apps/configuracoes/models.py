from django.db import models
from django.core.exceptions import ValidationError
from fernet_fields.fields import EncryptedTextField

class ConfiguracoesWhatsapp(models.Model):
    instancia = models.CharField(max_length=100)
    token = EncryptedTextField()
    client_token = EncryptedTextField(null=True, blank=True)
    url_base = models.URLField(max_length=2000)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Configuração API Whatsapp"
        verbose_name_plural  = "Configurações API Whatsapp"
        constraints = [
        models.UniqueConstraint(
            fields=["ativo"],
            condition=models.Q(ativo=True),
            name="unique_config_whatsapp_ativa"
        )]


    def clean(self):
        if self.ativo:
            qs = ConfiguracoesWhatsapp.objects.filter(ativo=True)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError("Já existe uma configuração WhatsApp ativa.")

    def __str__(self):
        return f"Whatsapp {self.instancia}"
       



