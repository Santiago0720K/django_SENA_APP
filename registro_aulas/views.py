from django.http import HttpResponse
from django.template import loader
from .models import Aulas
from .forms import AulasForm

def lista_aulas(request):
    lista_aulas = Aulas.objects.all()
    template = loader.get_template('lista_aulas.html')
    context = {
        'lista_aulas': lista_aulas,
        'total_aulas': lista_aulas.count(),
    }
    return HttpResponse(template.render(context, request))

def registrar_aula(request):
    if request.method == 'POST':
        form = AulasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Aula registrada exitosamente.")
    else:
        form = AulasForm()
    template = loader.get_template('registro_aulas.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))