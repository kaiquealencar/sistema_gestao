import pytest
from servicos.models import Servico

@pytest.mark.django_db
def test_criar_servico():
    servico = Servico.objects.create(
        nome="Site institucional",
        preco=1500.00,
        disponivel=True,
        ativo=True
    )
    assert servico.id is not None