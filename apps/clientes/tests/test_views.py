import pytest
from  django.urls import reverse
from apps.clientes.models import Cliente
from decimal import Decimal

@pytest.mark.django_db
def test_cliente_list_view(client):
    Cliente.objects.create(
        nome="Cliente Válido",
        tipo_cliente="PF",
        cpf_cnpj="933.614.720-08",
        email="example@example.com.br",
        telefone="(12) 36589-875",
        cep="12287-020",
        logradouro="Rua Exemplo",
        numero="123",
        bairro="Bairro Exemplo",
        cidade="Cidade Exemplo",
        estado="SP",
        observacoes="Observações do cliente",
        ativo=True
    )

    url = reverse('clientes:cliente_list')
    response = client.get(url)

    assert response.status_code == 200
    assert "Cliente Válido" in response.content.decode()

@pytest.mark.django_db
def test_criar_cliente_view(client):
    url = reverse('clientes:cliente_create')
    data ={
        
        "nome": "Cliente Válido",
        "tipo_cliente":"PF",
        "cpf_cnpj": "933.614.720-08",
        "email":"example@example.com.br",
        "telefone":"(12) 36589-875",
        "cep":"12287-020",
        "logradouro": "Rua Exemplo",
        "numero":"123",
        "bairro":"Bairro Exemplo",
        "cidade":"Cidade Exemplo",
        "estado":"SP",
        "observacoes":"Observações do cliente",
        "ativo": True
    }

    reponse = client.post(url, data)

    assert reponse.status_code == 302      
    assert Cliente.objects.filter(nome="Cliente Válido").exists()


@pytest.mark.django_db
def test_criar_cliente_get(client):
    url = reverse('clientes:cliente_create')
    response = client.get(url)

    assert response.status_code == 200
    assert "form" in response.context
    