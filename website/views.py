from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def lista_funcionarios(request):
    return render(request, 'website/lista.html')
