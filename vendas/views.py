from django.shortcuts import render
from django.views.generic import CreateView
from .models import Venda
from django.urls import reverse_lazy


# Create your views here.

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("cadastrar_venda")








