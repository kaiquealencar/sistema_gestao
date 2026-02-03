import pytest
from decimal import Decimal
from django.core.exceptions import ValidationError
from apps.servicos.models import Servico

@pytest.mark.django_db
def test_criar_servico_valido():
    servico = Servico(
        nome="Serviço Válido",
        descricao="Descrição do serviço",
        preco=Decimal("150.00"),
        disponivel=True
    )
    servico.full_clean()
    servico.save()

    assert Servico.objects.count() == 1
    assert Servico.objects.first().nome == "Serviço Válido"


@pytest.mark.django_db
def test_servico_preco_negativo_gera_erro():
    servico = Servico(
        nome="Serviço Inválido",
        descricao="Descrição",
        preco=Decimal("-50.00"),
        disponivel=True
    )

    with pytest.raises(ValidationError) as excinfo:
        servico.full_clean()

    assert "O preço não pode ser negativo." in str(excinfo.value)


@pytest.mark.django_db
def test_str_retorna_nome():
    servico = Servico(
        nome="Serviço Teste",
        descricao="Descrição",
        preco=Decimal("100.00"),
        disponivel=True
    )
    assert str(servico) == "Serviço Teste"


@pytest.mark.django_db
def test_campos_ativos_e_disponiveis_padrao():
    servico = Servico(
        nome="Serviço Teste",
        descricao="Descrição",
        preco=Decimal("100.00")
    )
    servico.full_clean()
    servico.save()

    s = Servico.objects.first()
    assert s.ativo is True
    assert s.disponivel is True
