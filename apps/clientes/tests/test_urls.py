import pytest
from  django.urls import reverse
from django.test import Client
from apps.clientes.models import Cliente
from decimal import Decimal

@pytest.mark.django_db
def test_cliente_status_code(): 
    client = Client()   

    url_list = reverse('clientes:cliente_list')
    response = client.get(url_list) 
    assert response.status_code == 200
    assert url_list == '/clientes/'

    url_criar = reverse('clientes:cliente_create')
    response = client.get(url_criar)
    assert response.status_code == 200    
    assert url_criar == '/clientes/cadastrar/'

    c = Cliente.objects.create(
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

    url_editar = reverse('clientes:cliente_edit', args=[c.id])
    assert url_editar == f'/clientes/{c.id}/editar/'
    response = client.get(url_editar)

    url_deletar = reverse('clientes:cliente_delete', args=[c.id])
    assert response.status_code == 200
    assert url_deletar == f'/clientes/{c.id}/excluir/'
    