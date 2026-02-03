from django import forms
from django.forms import inlineformset_factory
from .models import Orcamento, ItemOrcamento
from apps.servicos.models import Servico

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['cliente', 'validade', 'status', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'validade': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields = ['servico', 'quantidade', 'preco']
        widgets = {
            'servico': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

ItemOrcamentoFormSet = inlineformset_factory(
    Orcamento,               
    ItemOrcamento,            
    form=ItemOrcamentoForm,   
    extra=1,                  
    can_delete=True           
)
