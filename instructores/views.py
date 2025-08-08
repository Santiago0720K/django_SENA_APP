from django.views.generic import ListView, DetailView
from .models import Instructor

class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructores/lista_instructores.html'
    context_object_name = 'lista_instructores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_instructores'] = self.get_queryset().count()
        return context

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructores/detalle_instructor.html'
    context_object_name = 'instructor'