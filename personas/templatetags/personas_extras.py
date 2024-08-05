from django import template
from personas.models import Persona

register = template.Library()

@register.simple_tag
def get_persona_list():
    personas = Persona.objects.all()
    return personas