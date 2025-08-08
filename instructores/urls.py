from django.urls import path
from .views import InstructorListView, InstructorDetailView

app_name = 'instructores'

urlpatterns = [
    path('lista/', InstructorListView.as_view(), name='lista_instructores'),
    path('detalle/<int:pk>/', InstructorDetailView.as_view(), name='detalle_instructor'),
]