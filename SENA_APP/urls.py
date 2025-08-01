from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),
    path('', include('instructores.urls')),
    path('', include('programas.urls')),
]
