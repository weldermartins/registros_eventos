from django.contrib import admin

# Register your models here.
from registro_aprendizados.models import Topico, Assuntos
admin.site.register(Topico)
admin.site.register(Assuntos)
