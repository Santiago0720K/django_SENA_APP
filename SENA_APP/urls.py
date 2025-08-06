from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),
    path('', include('instructores.urls')),
    path('', include('programas.urls')),
]

# Personalización del panel administrativo
admin.site.site_header = "Panel Administrativo SENA"
admin.site.site_title = "SENA APP"
admin.site.index_title = "Gestión de Aprendices"