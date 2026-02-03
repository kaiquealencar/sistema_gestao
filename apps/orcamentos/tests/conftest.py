import pytest
from django.utils import timezone
from apps.orcamentos.models import Orcamento
from apps.clientes.models import Cliente


@pytest.fixture
def cliente(db):
    return Cliente.objects.create(
        nome="Cliente Teste",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="teste@email.com"
    )


@pytest.fixture
def orcamento(cliente):
    return Orcamento.objects.create(
        cliente=cliente,
        validade=timezone.now() + timezone.timedelta(days=30)
    )
