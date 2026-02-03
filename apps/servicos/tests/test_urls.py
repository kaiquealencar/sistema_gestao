import pytest
from  django.urls import reverse
from django.test import Client
from apps.servicos.models import Servico
from decimal import Decimal

@pytest.mark.django_db
def test_servico_status_code():
    client = Client()

    url_list = reverse('servicos:servico_list')
    response = client.get(url_list)
    assert response.status_code == 200
    assert url_list == '/servicos/'

    url_criar = reverse('servicos:servico_create')
    response = client.get(url_criar)    
    assert response.status_code == 200
    assert url_criar == '/servicos/novo/'

    servico = Servico.objects.create(
        nome="Teste URL serviço", 
        descricao="Descrição", 
        preco=Decimal("150.00"), 
        disponivel=True)
    
    url_editar = reverse('servicos:servico_edit', args=[servico.id])
    response = client.get(url_editar)   
    assert response.status_code == 200
    assert url_editar == f'/servicos/{servico.id}/editar/'

    
    url_deletar = reverse('servicos:servico_delete', args=[servico.id])
    response = client.get(url_deletar)      
    assert response.status_code == 200
    assert url_deletar == f'/servicos/{servico.id}/excluir/'
