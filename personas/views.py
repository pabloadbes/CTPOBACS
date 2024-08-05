from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Persona

# Create your views here.
class PersonaListView(ListView):
    model = Persona

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreate(CreateView):
    model = Persona
    fields = ['nombre', 'apellido', 'dni']
    success_url = reverse_lazy('personas:personas')