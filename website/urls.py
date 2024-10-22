from django.urls import path
from .views import IndexTemplateView
from .views import ListaFuncionarios
from .views import FuncionarioUpdateView

app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('lista', ListaFuncionarios.as_view(), name='lista'),
    path('atualiza/<id>', FuncionarioUpdateView.as_view(), name='atualiza')
]
