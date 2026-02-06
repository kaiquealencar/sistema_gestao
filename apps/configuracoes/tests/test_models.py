import pytest
from django.core.exceptions import ValidationError
from apps.configuracoes.models import ConfiguracoesWhatsapp

@pytest.mark.django_db
def test_criar_config_valido():
    config = ConfiguracoesWhatsapp(
       nome_instancia="58291038475629103847562910384756",
       token="842095317659284061374592",
       client_token="8492037561849302756102938475610293",
       url_base="http://localhost:8000/api/v1/"      
    )    
    config.full_clean()
    config.save()

    assert ConfiguracoesWhatsapp.objects.count() == 1
    assert ConfiguracoesWhatsapp.objects.first().url_base == "http://localhost:8000/api/v1/"
