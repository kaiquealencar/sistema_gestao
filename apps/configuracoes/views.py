from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .forms import ConfiguracoesForm
from .models import ConfiguracoesWhatsapp


def config_view(request):
    config = ConfiguracoesWhatsapp.objects.first()
    form = ConfiguracoesForm(request.POST or None, instance = config)

    if request.method == "POST" and form.is_valid():
      form.save()
      messages.success(request, "Configuração salva com sucesso!")  

      return redirect("config:config_view")

    return render(request, "configuracoes/config_form.html", {"form": form})
