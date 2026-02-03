import pytest
from django.urls import reverse, resolve
from apps.orcamentos import views


def test_orcamento_list_url():
    url = reverse("orcamentos:orcamento_list")
    resolver = resolve(url)
    assert resolver.func == views.orcamento_list


def test_orcamento_create_url():
    url = reverse("orcamentos:orcamento_create")
    resolver = resolve(url)
    assert resolver.func == views.orcamento_create


def test_orcamento_detail_url():
    url = reverse("orcamentos:orcamento_detail", args=[1])
    resolver = resolve(url)
    assert resolver.func == views.orcamento_detail


def test_orcamento_edit_url():
    url = reverse("orcamentos:orcamento_edit", args=[1])
    resolver = resolve(url)
    assert resolver.func == views.orcamento_edit


def test_orcamento_delete_url():
    url = reverse("orcamentos:orcamento_delete", args=[1])
    resolver = resolve(url)
    assert resolver.func == views.orcamento_delete
