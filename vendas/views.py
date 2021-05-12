from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from .models import Venda, Produto
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import VendaForm, VendaObservacaoForm, VendaClienteForm
# Create your views here.


class VendaCreateView(CreateView):
    form_class = VendaForm
    template_name = 'cadastrar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com suceso!')
        return reverse_lazy("listar_venda")


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    # Caso eu queira que sejam cadastrados todos os fields do meu Model você colocará o fields = '__all__'
    # Caso queira especificar, colocar da forma abaixo. Por exemplo, se quiser apenas nome colocar fields = ['nome']
    fields = ['nome', 'valor']

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse_lazy('cadastrar_produto')


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


class VendaCorrecaoUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')

class VendaAtualizarObservacaoView(UpdateView):
    model = Venda
    form_class = VendaObservacaoForm
    template_name = 'atualizar/venda_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')

class VendaAtualizarClienteView(UpdateView):
    model = Venda
    form_class = VendaClienteForm
    template_name = 'atualizar/venda_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class VendaView(View):
    def desabilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))

    def habilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'detalhes/venda.html'