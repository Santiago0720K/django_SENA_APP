from django.urls import path
from . import views

app_name = 'registro_aulas'

urlpatterns = [
    path('aulas/', views.lista_aulas, name='lista_aulas'),
    path("aulas/registro/", views.registrar_aula, name='registro_aulas'),
]