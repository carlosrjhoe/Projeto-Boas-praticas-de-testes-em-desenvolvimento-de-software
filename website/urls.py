from django.urls import path
from .views import IndexView
from .views import ListaFuncionarios

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view()),
    path('lista', ListaFuncionarios.as_view())
]
