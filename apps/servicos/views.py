from email.mime import message
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .forms import ServicoForm
from .models import Servico


def servico_create(request):
    form = ServicoForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        servico = form.save()
        servico.ativo = False if "ativo" not in form.cleaned_data else form.cleaned_data["ativo"]
        servico.full_clean()
        servico.save()

        messages.success(request, "Serviço cadastrado com sucesso!")

        return redirect('servicos:servico_list')

    return render(request, 'servicos/servico_form.html', {'form': form})

def servico_list(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/servico_list.html', {'servicos': servicos})

def servico_edit(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    form = ServicoForm(request.POST or None, instance=servico)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Serviço {servico.nome} atualizado com sucesso!")
        return redirect('servicos:servico_list')


    return render(request, 'servicos/servico_form.html', {"form": form, "servico": servico, "editando": True})

def servico_delete(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    if request.method == "POST":
        servico.delete()
        messages.success(request, f"Serviço {servico.nome} excluído com sucesso!")
        
        return redirect('servicos:servico_list')
    return render(request, 'servicos/servico_list.html', {'servico_id': servico_id})