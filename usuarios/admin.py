from django.contrib import admin

from .models import Centro_asistencial, Ubicacion, Paciente

class Centro_asistencialAdmin(admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(Centro_asistencial, Centro_asistencialAdmin)
admin.site.register(Ubicacion)
admin.site.register(Paciente)