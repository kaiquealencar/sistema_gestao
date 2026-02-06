import pytest
from  django.urls import reverse
from apps.configuracoes.models import ConfiguracoesWhatsapp


@pytest.mark.django_db
def test_config_create_view(client):
    url = reverse("config:config_create")
    data = {
        "instancia": "58291038475629103847562910384756",
        "token": "842095317659284061374592",
        "client_token": "8492037561849302756102938475610293",
         "url_base": "http://localhost:8000/api/v1/"  ,
        "ativo": True,
    }

    response = client.post(url, data)
    assert response.status_code == 302

    assert response.url == reverse("config:config_list")
    assert ConfiguracoesWhatsapp.objects.filter(url_base="http://localhost:8000/api/v1/").exists()
