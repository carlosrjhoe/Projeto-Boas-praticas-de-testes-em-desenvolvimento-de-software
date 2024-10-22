from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Funcionario

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'website\index.html'


class ListaFuncionarios(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'


def criar_funcionario(request):
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website/lista.html'))
    else:
        return render(request, 'website.form.html', {'form':form})


class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = '__all__'

    def get_object(self, queryset=None):
        funcionario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            funcionario = Funcionario.objects.filter(id=id).first()
        elif slug is not None:
            # Pega o campo slug do Model
            campo_slug = self.get_slug_field()
            # Busca o funcionario apartir do slug
            funcionario = Funcionario.objects.filter(
                **{campo_slug: slug}
            ).first()
            
        return funcionario


class FuncionarioDeleteView(DeleteView):
    template_name = 'website/excluir.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista')