import pytest
from django.urls import reverse
from apps.orcamentos.models import Orcamento, ItemOrcamento

@pytest.mark.django_db
def test_orcamento_list_view(client):
    url = reverse("orcamentos:orcamento_list")
    response = client.get(url)
    assert response.status_code == 200
    assert "orcamentos/orcamento_list.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_orcamento_create_view_get(client):
    url = reverse("orcamentos:orcamento_create")
    response = client.get(url)
    assert response.status_code == 200
    assert "orcamentos/orcamento_form.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_orcamento_create_post_success(client, cliente, servico):
    url = reverse("orcamentos:orcamento_create")
    s1, _ = servico
    
    payload = {
        'cliente': cliente.id,
        'validade': '2026-12-31',
        'status': 'pendente',
        'observacoes': 'Novo orçamento',
        'itemorcamento_set-TOTAL_FORMS': '1',
        'itemorcamento_set-INITIAL_FORMS': '0',
        'itemorcamento_set-MIN_NUM_FORMS': '0',
        'itemorcamento_set-MAX_NUM_FORMS': '1000',
        'itemorcamento_set-0-servico': s1.id,
        'itemorcamento_set-0-quantidade': 2,
        'itemorcamento_set-0-preco': 150.00,
    }
    
    response = client.post(url, payload)
    
    assert response.status_code == 302 
    assert Orcamento.objects.count() == 1
    assert ItemOrcamento.objects.count() == 1


@pytest.mark.django_db(transaction=True)
def test_orcamento_edit_post_delete_item(client, orcamento, servico):
    url = reverse("orcamentos:orcamento_edit", args=[orcamento.id])
    s1, s2 = servico

    item1 = ItemOrcamento.objects.create(orcamento=orcamento, servico=s1, quantidade=2, preco=100)
    item2 = ItemOrcamento.objects.create(orcamento=orcamento, servico=s2, quantidade=1, preco=200)

    itens = ItemOrcamento.objects.filter(orcamento=orcamento)
    print(f"\n--- DEBUG FINAL ---")
    print(f"Itens no banco para este orçamento: {itens.count()}")
    
    assert itens.count() == 2

    payload = {
        'cliente': orcamento.cliente.id,
        'validade': orcamento.validade.strftime('%Y-%m-%d'),
        'status': orcamento.status,
        
        'itemorcamento_set-TOTAL_FORMS': '2',
        'itemorcamento_set-INITIAL_FORMS': '2',
        'itemorcamento_set-MIN_NUM_FORMS': '0',
        'itemorcamento_set-MAX_NUM_FORMS': '1000',
        
        'itemorcamento_set-0-id': item1.id,
        'itemorcamento_set-0-servico': s1.id,
        'itemorcamento_set-0-quantidade': '2',
        'itemorcamento_set-0-preco': '100.00',
        'itemorcamento_set-0-DELETE': 'on', # O sinal da lixeira!

        'itemorcamento_set-1-id': item2.id,
        'itemorcamento_set-1-servico': s2.id,
        'itemorcamento_set-1-quantidade': '1',
        'itemorcamento_set-1-preco': '200.00',
    }

    response = client.post(url, payload)

    assert response.status_code == 302 
    
    assert ItemOrcamento.objects.filter(id=item1.id).count() == 0
    assert ItemOrcamento.objects.filter(id=item2.id).count() == 1


@pytest.mark.django_db
def test_orcamento_detail_view(client, orcamento):
    url = reverse("orcamentos:orcamento_detail", args=[orcamento.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["orcamento"] == orcamento

@pytest.mark.django_db
def test_orcamento_delete_view(client, orcamento):
    url = reverse("orcamentos:orcamento_delete", args=[orcamento.id])
    response = client.post(url)
    assert response.status_code == 302
    assert not Orcamento.objects.filter(id=orcamento.id).exists()