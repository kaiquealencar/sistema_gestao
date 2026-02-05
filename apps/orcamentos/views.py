from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from weasyprint import HTML
from django.http import HttpResponse
from services.whatsapp import enviar_whatsapp_mensagem
from services.utils import normalizar_telefone

from .forms import OrcamentoForm, ItemOrcamentoFormSet
from .models import Orcamento


def orcamento_list(request):
    status = request.GET.get('status')
    queryset = Orcamento.objects.all().order_by('-data_criacao')

    if status:
        queryset = queryset.filter(status=status)

    return render(request, 'orcamentos/orcamento_list.html', {
        'orcamentos': queryset
    })


def orcamento_create(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        formset = ItemOrcamentoFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            orcamento = form.save()
            formset.instance = orcamento
            formset.save()


            messages.success(request, "Orçamento criado com sucesso!")
            return redirect('orcamentos:orcamento_list')
    else:
        form = OrcamentoForm()
        formset = ItemOrcamentoFormSet()

    return render(request, 'orcamentos/orcamento_form.html', {
        'form': form,
        'formset': formset
    })


def orcamento_edit(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)

    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        formset = ItemOrcamentoFormSet(request.POST, instance=orcamento)

        if form.is_valid() and formset.is_valid():
            form.save()      
            formset.save()
            messages.success(request, "Orçamento atualizado com sucesso!")
            return redirect('orcamentos:orcamento_list')
    else:
        form = OrcamentoForm(instance=orcamento)
        formset = ItemOrcamentoFormSet(instance=orcamento)

    return render(request, 'orcamentos/orcamento_form.html', {
        'form': form,
        'formset': formset,
        'editando': True
    })


def orcamento_delete(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)

    if request.method == 'POST':
        orcamento.delete()
        messages.success(request, "Orçamento excluído com sucesso!")
        return redirect('orcamentos:orcamento_list')

    return render(request, 'orcamentos/orcamento_confirm_delete.html', {
        'orcamento': orcamento
    })


def orcamento_detail(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    return render(request, 'orcamentos/orcamento_detail.html', {
        'orcamento': orcamento
    })


def exportar_orcamento_pdf(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    html_string = render_to_string('orcamentos/orcamento_pdf.html', {'orcamento': orcamento})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf_content = html.write_pdf()

    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="orcamento_{orcamento.id}.pdf"'
    #response['Content-Disposition'] = f'attachment; filename="orcamento_{orcamento.id}.pdf"'
    return response 

def enviar_orcamento_whatsapp(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    
    mensagem =  f"Olá {orcamento.cliente.nome}, aqui está o seu orçamento:\n\n"


    for item in orcamento.itemorcamento_set.all():
        mensagem += f"- {item.servico.nome}: R$ {item.preco:.2f}\n"
    mensagem += f"\nTotal: R$ {orcamento.total:.2f}"

    try:        
        enviar_whatsapp_mensagem(normalizar_telefone(orcamento.cliente.telefone), mensagem)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({'status': 'success'})
        
        messages.success(request, "Orçamento enviado via WhatsApp!")
        return redirect('orcamentos:orcamento_detail', id=orcamento.id)
    except Exception as e:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        messages.error(request, f"Erro: {str(e)}")
        return redirect('orcamentos:orcamento_detail', id=orcamento.id)

'''
    mensagem =  f"Olá {orcamento.cliente.nome}, aqui está o seu orçamento:\n\n"

    for item in orcamento.itemorcamento_set.all():
        mensagem += f"- {item.servico.nome}: R$ {item.preco:.2f}\n"
    mensagem += f"\nTotal: R$ {orcamento.total:.2f}"
    
    enviar_whatsapp_mensagem(normalizar_telefone(orcamento.cliente.telefone), mensagem)
    messages.success(request, "Orçamento enviado via WhatsApp com sucesso!")
    return redirect('orcamentos:orcamento_detail', id=orcamento.id)
'''
