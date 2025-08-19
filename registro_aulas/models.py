from django.db import models

class Aulas(models.Model):
    TIPO_AULA_CHOICES = [
        ('Aula Teórica'),
        ('Laboratorio'),
        ('Taller'),
        ('Auditorio'),
        ('Sala de computo'),
        ('Biblioteca'),
        ('Multipropósito'),
    ]
    
    UBICACION_CHOICES = [
        ('Centro Minero'),
        ('CEDEAGRO'),
        ('CEGAFE'),
        ('Sede Sogamoso'),
    ]
    
    numero_aula = models.CharField(max_length=10, unique=True, verbose_name='Número de Aula')
    nombre_aula = models.CharField(max_length=100, verbose_name='Nombre del Aula')
    tipo_aula = models.CharField(max_length=50, choices=TIPO_AULA_CHOICES, verbose_name='Tipo de Aula')
    capacidad = models.PositiveIntegerField(verbose_name='Capacidad del Aula')
    ubicacion = models.CharField(max_length=50, choices=UBICACION_CHOICES, verbose_name='Ubicación')

    # Se agregan los campos booleanos para los equipos
    proyector = models.BooleanField(default=False, verbose_name='Proyector')
    tablero_digital = models.BooleanField(default=False, verbose_name='Tablero Digital')
    computadores = models.BooleanField(default=False, verbose_name='Computadores')
    sistema_sonido = models.BooleanField(default=False, verbose_name='Sistema de Sonido')
    aire_acondicionado = models.BooleanField(default=False, verbose_name='Aire Acondicionado')
    wifi = models.BooleanField(default=False, verbose_name='WiFi')

    estado_aula = models.CharField(max_length=50, verbose_name='Estado del Aula')
    descripcion_adicional = models.TextField(blank=True, verbose_name='Descripción Adicional')
    
    def __str__(self):
        return f"{self.numero_aula} - {self.nombre_aula} ({self.tipo_aula})"
    