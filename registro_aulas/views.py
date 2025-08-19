from django.http import HttpResponse
from django.template import loader
from .models import Aulas

def aulas(request):
    lista_aulas = Aulas.objects.all()
    template = loader.get_template('registro_aulas.html')
    context = {
        'lista_aulas': lista_aulas,
        'total_aulas': lista_aulas.count(),
    }
    return HttpResponse(template.render(context, request))
