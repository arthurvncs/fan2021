from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['nome', 'valor', 'numero_venda', 'observacao', 'comprovante_venda', 'exemplo_upload',
                  'produtos', 'cliente', 'novo_item']


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']