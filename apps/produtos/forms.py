from django import forms
from common.forms import BaseForm
from .models import Produtos

class ProdutoForm(BaseForm):
    class Meta:
        model = Produtos
        fields = "__all__"
        exclude = ["codigo"]
        
        labels = {
            "nome": "Nome do Produto",
            "descricao": "Descrição do Produto",
            "Categoria": "Categoria",
            "codigo": "Código do Sistema",
            "preco_custo": "Preço de Custo",
            "preco_venda": "Preço de Venda",
            "quantidade_estoque": "Quantidade de Estoque",
            "estoque_minimo": "Estoque Mínimo do Produto",
            "unidade_medida": "Unidade de Medida (UN)",
            "fornecedor": "Fornecedor",
            "imagem": "Foto do Produto",
            "codigo_barras": "Código de Barras",
            "ativo": "Ativo"
        }

        widgets = {
            "nome": forms.TextInput(attrs={"id": "nome", "class": "form-control"}),
            "descricao": forms.TextInput(attrs={"id": "descricao", "class": "form-control"}),
            "Categoria": forms.Select({"id": "categoria", "class": "form-select"}),
            "codigo": forms.TextInput(attrs={"id": "codigo_sistema", "class": "form-control", "disabled": True}),
            "preco_custo": forms.TextInput(attrs={"id": "preco_custo", "class": "form-control"}),
            "preco_venda": forms.TextInput(attrs={"id": "preco_venda", "class": "form-control"}),
            "quantidade_estoque": forms.TextInput(attrs={"id": "qtd_estoque", "class": "form-control"}),
            "estoque_minimo": forms.TextInput(attrs={"id": "qtd_estoque_min", "class": "form-control"}),
            "unidade_medida": forms.TextInput(attrs={"id": "un", "class": "form-control"}),
            "fornecedor": forms.TextInput(attrs={"id": "fornecedor", "class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            "codigo_barras": forms.TextInput(attrs={"id": "cod_barras", "class": "form-control"}),
            "ativo":  forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


