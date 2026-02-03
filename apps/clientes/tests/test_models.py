import pytest
from django.core.exceptions import ValidationError
from apps.clientes.models import Cliente

@pytest.mark.django_db
def test_criar_cliente_valido():
    cliente = Cliente(
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

    cliente.full_clean()
    cliente.save()

    c = Cliente.objects.first()

    assert c.cpf_cnpj == "93361472008"
    assert c.telefone == "1236589875"
    assert c.cep == "12287020"

    assert c.cpf_cnpj_formatado == "933.614.720-08"
    assert c.telefone_formatado == "(12) 3658-9875"
    assert c.cep_formatado == "12287-020"

    assert c.nome == "Cliente Válido"
    assert c.email == "example@example.com.br"
    assert c.tipo_cliente == "PF"
    assert c.ativo is True


@pytest.mark.django_db
def test_criar_cliente_com_cpf_invalido():
    cliente = Cliente(
        nome="Maria",
        tipo_cliente="PF",
        cpf_cnpj="684.961.990-0", 
        email="maria@example.com"
    )

    with pytest.raises(ValidationError) as e:
        cliente.full_clean()

    assert "CPF deve ter 11 dígitos" in str(e.value)


@pytest.mark.django_db
def test_criar_cliente_com_cnpj_invalido():
    cliente = Cliente(
        nome="Empresa X",
        tipo_cliente="PJ",
        cpf_cnpj="12.345.678/0001-9",  
        email="empresa@example.com"
    )

    with pytest.raises(ValidationError) as e:
        cliente.full_clean()

    assert "CNPJ deve ter 14 dígitos" in str(e.value)


@pytest.mark.django_db
def test_criar_cliente_com_telefone_invalido():
    cliente = Cliente(
        nome="Teste Telefone",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="teste@example.com",
        telefone="1234"  
    )

    with pytest.raises(ValidationError) as e:
        cliente.full_clean()

    assert "Telefone inválido" in str(e.value)


@pytest.mark.django_db
def test_criar_cliente_com_cep_invalido():
    cliente = Cliente(
        nome="Teste CEP",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="teste@example.com",
        cep="12345"  
    )

    with pytest.raises(ValidationError) as e:
        cliente.full_clean()

    assert "CEP inválido" in str(e.value)


@pytest.mark.django_db
def test_limpeza_mascara_telefone_cep_cpf_cnpj():
    cliente = Cliente(
        nome="Cliente Máscara",
        tipo_cliente="PF",
        cpf_cnpj="933.614.720-08",
        email="mask@example.com",
        telefone="(12) 98765-4321",
        cep="12287-020"
    )

    cliente.full_clean()
    cliente.save()

    c = Cliente.objects.first()

    assert c.cpf_cnpj == "93361472008"
    assert c.telefone == "12987654321"
    assert c.cep == "12287020"

    assert c.cpf_cnpj_formatado == "933.614.720-08"
    assert c.telefone_formatado == "(12) 98765-4321"
    assert c.cep_formatado == "12287-020"


@pytest.mark.django_db
def test_cliente_ativo_padrao():
    cliente = Cliente(
        nome="Ativo Teste",
        tipo_cliente="PF",
        cpf_cnpj="93361472008",
        email="ativo@example.com"
    )

    cliente.full_clean()
    cliente.save()
    c = Cliente.objects.first()
    assert c.ativo is True
