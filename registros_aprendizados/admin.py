from django.contrib import admin

# Register your models here.
from registros_aprendizados.models import Topico, Assuntos
admin.site.register(Topico)
admin.site.register(Assuntos)
