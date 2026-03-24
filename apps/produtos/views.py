from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, CharField, TextField
from django.http import HttpResponse
from .forms import ProdutoForm
from .models import Produtos

@login_required
def produto_create(request):
    print("FILES >>>", request.FILES)
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if  form.is_valid():
            produto = form.save()
            produto.ativo = form.cleaned_data.get("ativo", False)
            produto.save()

            messages.success(request, "produto cadastrado com sucesso!")
            return redirect("produtos:produto_list")
        else:
            messages.error(request, "Erro ao cadastrar o produto. Verifique os campos.")
    

    return render(request, "produtos/produtos_forms.html", {"form": form})

@login_required
def produto_edit(request, id):
    produto = get_object_or_404(Produtos, id=id)    
    form = ProdutoForm(request.POST or None, request.FILES or None,  instance=produto)

    if request.method == "POST":            
      if form.is_valid():
       
        if not request.FILES.get("imagem"):
            form.instance.imagem = produto.imagem

        form.save()
        messages.success(request, f"Produto {produto.nome} atualizado com sucesso!")

        return redirect('produtos:produto_list')
      else:
          messages.error(request, "Erro ao atualizar o produto.")
    
    return render(request, "produtos/produtos_forms.html", {"form": form, "editando": True, "produto": produto})
    
@login_required
def produto_list(request):  
    produtos = Produtos.objects.all().order_by("id")
    termo = request.GET.get("search", "").strip()

    if termo:
        query = Q()
        for field in Produtos._meta.get_fields():
            if isinstance(field, (CharField, TextField)):
                query |= Q(**{f"{field.name}__icontains": termo})
     
        produtos = produtos.filter(query)
    

    return render(request, "produtos/produtos_list.html", {"produtos": produtos, "termo": termo})

@login_required
def produto_delete(request, id):
    produto = get_object_or_404(Produtos, id=id)
         
    if request.method == "POST":
        produto.delete()
        messages.success(request, f"Produto {produto.nome} excluído com sucesso!")
        
        return redirect('produtos:produto_list')
    
    return render(request, 'produtos/produtos_list.html', {'id': id})
