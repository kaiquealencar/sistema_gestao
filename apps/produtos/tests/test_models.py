import pytest
from decimal import Decimal
from apps.produtos.models import Produtos

@pytest.mark.django_db
def test_criar_produto():
    produto = Produtos(
        nome="Produto Teste",
        descricao="Descrição teste",
        categoria="Categoria Teste",
        preco_custo=Decimal("5.00"),
        preco_venda=Decimal("10.00"),
        quantidade_estoque=10,
        estoque_minimo=5,
        unidade_medida="Lt",
        fornecedor="Fornecedor teste",
        ativo=True
    )

    produto.full_clean()
    produto.save()

    assert Produtos.objects.count() == 1

    assert produto.codigo is not None
    assert len(produto.codigo) > 0
