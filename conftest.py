import pytest
from django.utils import timezone
from apps.orcamentos.models import Orcamento, ItemOrcamento
from apps.clientes.models import Cliente
from apps.servicos.models import Servico


@pytest.fixture
def cliente(db):
    c = Cliente.objects.create(
        nome="Cliente Teste",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="example@example.com"
    )
    return c

@pytest.fixture
def servico(db):
    s1 = Servico.objects.create(nome="Serviço A", preco=150.00)
    s2 = Servico.objects.create(nome="Serviço B", preco=250.00)
    return s1, s2

@pytest.fixture
def orcamento(db, cliente):
    from apps.orcamentos.models import Orcamento
    from django.utils import timezone
    
    return Orcamento.objects.create(
        cliente=cliente,
        validade=timezone.now().date() + timezone.timedelta(days=30),
        status="pendente"
    )