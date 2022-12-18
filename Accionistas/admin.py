from django.contrib import admin

from .models import Accionista

# Register your models here.
class AccionistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'activo']

admin.site.register(Accionista, AccionistaAdmin)
