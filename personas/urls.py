from django.urls import path
from .views import PersonaListView, PersonaDetailView, PersonaCreate

personas_patterns = ([
    path('', PersonaListView.as_view(), name='personas'),
    path('<int:pk>/<slug:slug>/', PersonaDetailView.as_view(), name='persona'),
    path('create/', PersonaCreate.as_view(), name='create'),
], 'personas')