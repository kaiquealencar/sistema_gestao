from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import ProdutoForm
from .models import Produtos

def produto_create(request):
    form = ProdutoForm()
    if request.method == "POST" and form.is_valid():
        produto = form.save()
        produto.ativo = False if "ativo" not in form.cleaned_data else form.cleaned_data["ativo"]
        produto.save()

        messages.success(request, "produto cadastrado com sucesso!")
        return redirect("produto:produtos_list")
    

    return render(request, "produtos/produtos_forms.html", {"form": form})

def produto_edit(request, id):
    produto = get_object_or_404(Produtos, id=id)

    form = ProdutoForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
      form.save()
      messages.success(request, f"Produto {produto.nome} atualizado com sucesso!")
      return redirect('produtos:produtos_list')

    
    return render(request, "produtos/produtos_forms.html", {"form": form, "editando": True})
    

def produto_list(request):
    produtos = Produtos.objects.all()

    return render(request, "produtos/produtos_list", {"produto": produtos})