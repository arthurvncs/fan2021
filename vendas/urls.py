from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView


urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name='listar_venda'),
]