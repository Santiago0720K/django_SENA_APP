from django import forms
from .models import Aulas

class AulasForm(forms.ModelForm):
    class Meta:
        model = Aulas
        fields = [
            'numero_aula',
            'nombre_aula',
            'tipo_aula',
            'capacidad',
            'ubicacion',
            'proyector',
            'tablero_digital',
            'computadores',
            'sistema_sonido',
            'aire_acondicionado',
            'wifi',
            'estado_aula',
            'descripcion_adicional',
        ]
        labels = {
            'numero_aula': 'Número de Aula',
            'nombre_aula': 'Nombre del Aula',
            'tipo_aula': 'Tipo de Aula',
            'capacidad': 'Capacidad del Aula',
            'ubicacion': 'Ubicación',
            'proyector': 'Proyector',
            'tablero_digital': 'Tablero Digital',
            'computadores': 'Computadores',
            'sistema_sonido': 'Sistema de Sonido',
            'aire_acondicionado': 'Aire Acondicionado',
            'wifi': 'WiFi',
            'estado_aula': 'Estado del Aula',
            'descripcion_adicional': 'Descripción Adicional',
        }
        widgets = {
            'numero_aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 101'}),
            'nombre_aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Aula de Programación'}),
            'tipo_aula': forms.Select(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 30'}),
            'ubicacion': forms.Select(attrs={'class': 'form-control'}),
            'estado_aula': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_adicional': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }