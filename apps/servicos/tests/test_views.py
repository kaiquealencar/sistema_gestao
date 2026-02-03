import pytest
from  django.urls import reverse
from apps.servicos.models import Servico
from decimal import Decimal

@pytest.mark.django_db
def test_lista_servicos_view(client):
    Servico.objects.create(nome="Teste view serviço", descricao="Descrição", preco=Decimal("100.00"), disponivel=True)

    url = reverse('servicos:servico_list')
    response = client.get(url)

    assert response.status_code == 200
    assert "Teste view serviço" in response.content.decode()

  
@pytest.mark.django_db
def test_criar_servico_view(client):
    url = reverse('servicos:servico_create')
    data = {
        "nome": "Serviço via View",
        "descricao": "Descrição do serviço via view",
        "preco": "200.00",
        "disponivel": True,
        "ativo": True
    }
    response = client.post(url, data)

    assert response.status_code == 302      
    assert Servico.objects.filter(nome="Serviço via View").exists()

@pytest.mark.django_db
def test_criar_servico_get(client):
    url = reverse('servicos:servico_create')
    response = client.get(url)

    assert response.status_code == 200
    assert "form" in response.context