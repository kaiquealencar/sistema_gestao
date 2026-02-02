import pytest
from django.urls import reverse
from servicos.models import Servico

@pytest.mark.django_db
def test_criar_servico_view(client):
    url = reverse("servicos:servico_create")

    response = client.post(url, {
        "nome": "Consultoria",
        "preco": 200.00,
        "disponivel": True,
        "ativo": True
    })

    assert response.status_code == 302
    assert Servico.objects.count() == 1
