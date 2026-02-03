import pytest
from  django.urls import reverse
from apps.orcamentos.models import Orcamento


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
def test_orcamento_detail_view(client, orcamento):
    url = reverse("orcamentos:orcamento_detail", args=[orcamento.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["orcamento"] == orcamento


@pytest.mark.django_db
def test_orcamento_edit_view(client, orcamento):
    url = reverse("orcamentos:orcamento_edit", args=[orcamento.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["form"].instance == orcamento


@pytest.mark.django_db
def test_orcamento_delete_view(client, orcamento):
    url = reverse("orcamentos:orcamento_delete", args=[orcamento.id])
    response = client.post(url)

    assert response.status_code == 302 
