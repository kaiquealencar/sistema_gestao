import pytest
from django.utils import timezone
from apps.orcamentos.models import Orcamento, ItemOrcamento
from apps.clientes.models import Cliente
from apps.servicos.models import Servico

@pytest.fixture
def cliente(db):
    return Cliente.objects.create(
        nome="Cliente Teste",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="example@example.com"
    )

@pytest.fixture
def servico(db):
    s1 = Servico.objects.create(
        nome="Serviço A",
        descricao="Descrição do Serviço A",
        preco=150.00
    )
    s2 = Servico.objects.create(
        nome="Serviço B",
        descricao="Descrição do Serviço B",
        preco=250.00
    )
    return s1, s2

@pytest.fixture
def orcamento(cliente, servico, db):
    orc = Orcamento.objects.create(
        cliente=cliente,
        validade=timezone.now() + timezone.timedelta(days=30),
        status="pendente",
        observacoes="Orçamento de teste"
    )
    ItemOrcamento.objects.create(
        orcamento=orc,
        servico=servico[0],
        quantidade=2,
        preco=servico[0].preco
    )
    ItemOrcamento.objects.create(
        orcamento=orc,
        servico=servico[1],
        quantidade=1,
        preco=servico[1].preco
    )
    return orc

def test_orcamento_total(orcamento):
    assert orcamento.total == 550

def test_orcamento_status_default(orcamento):
    assert orcamento.status == "pendente"

def test_item_subtotal(orcamento, servico):
    s1, _ = servico
    item = orcamento.itemorcamento_set.get(servico=s1)
    assert item.subtotal == 300 
