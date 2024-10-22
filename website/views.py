from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Funcionario

# Create your views here.

class IndexView(TemplateView):
    template_name = 'website\index.html'


class ListaFuncionarios(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'
