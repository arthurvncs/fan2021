from django.contrib import admin
from django.urls import path
from .views import (
    VendaCreateView
    , ProdutoCreateView
    , VendaListView
    , VendaCorrecaoUpdateView
    , VendaAtualizarObservacaoView
    , VendaAtualizarClienteView
    , VendaView
    , VendaDetailView
)

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(), name="corrigir_venda"),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(), name="atualizar_observacao_venda"),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(), name="atualizar_cliente_venda"),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda, name="ajax_desabilitar_venda"),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda, name="ajax_habilitar_venda"),
    path('detalhes/venda/<int>:pl>', VendaDetailView.as_view(), name="detalhes_venda"),
]