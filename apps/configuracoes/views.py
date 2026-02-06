from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .forms import ConfiguracoesForm
from .models import ConfiguracoesWhatsapp

def config_create(request):
    form = ConfiguracoesForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        config = form.save(commit=False)
       # config.ativo = False if "ativo" not in form.cleaned_data else form.cleaned_data["ativo"]
        config.full_clean()
        config.save()

        messages.success(request, "Configurações salvas com sucesso!")

        return redirect("config:config_list")
    
    return render(request, "configuracoes/config_form.html", {"form": form})

def config_list(request):
    configs = ConfiguracoesWhatsapp.objects.all()
    return render(request, "configuracoes/config_list.html", {"configs": configs})
