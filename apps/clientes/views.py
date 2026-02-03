from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import ClienteForm
from .models import Cliente

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        cliente = form.save()
        cliente.ativo = False if "ativo" not in form.cleaned_data else form.cleaned_data["ativo"]
        cliente.save()

        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect('clientes:cliente_list')
    

    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_edit(request, cliente_id):    
    cliente = get_object_or_404(Cliente, id=cliente_id)
    form = ClienteForm(request.POST or None, instance=cliente)  

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Cliente {cliente.nome} atualizado com sucesso!")
        return redirect('clientes:cliente_list')
    
    return render(request, 'clientes/cliente_form.html', {'form': form, 'cliente': cliente, "editando": True})
    
def cliente_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.delete()
        messages.success(request, f"Cliente {cliente.nome} excluído com sucesso!")
        
    return redirect('clientes:cliente_list')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes_list.html', {'clientes': clientes})