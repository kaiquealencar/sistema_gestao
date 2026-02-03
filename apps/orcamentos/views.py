from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
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
            itens = formset.save(commit=False)

            for item in itens:
                item.orcamento = orcamento
                item.save()

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
