from django.contrib import admin
from .models import Persona

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')

admin.site.register(Persona, PersonaAdmin)
