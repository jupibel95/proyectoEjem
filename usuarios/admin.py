from django.contrib import admin

from .models import Centro_asistencial

class Centro_asistencialAdmin(admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(Centro_asistencial, Centro_asistencialAdmin)