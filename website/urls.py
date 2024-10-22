from django.urls import path
from .views import IndexTemplateView
from .views import ListaFuncionarios
from .views import FuncionarioUpdateView
from .views import FuncionarioDeleteView

app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('lista', ListaFuncionarios.as_view(), name='lista'),
    path('atualiza/<id>', FuncionarioUpdateView.as_view(), name='atualiza'),
    path('excluir/<id>', FuncionarioDeleteView.as_view(), name='excluir')
]
