from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    View responsável por renderizar a página inicial do site institucional.

    Utiliza TemplateView da biblioteca genérica de views do Django,
    permitindo associar um template HTML sem a necessidade de lógica adicional.

    URL associada: /
    Template utilizado: core/home.html
    """
    
    template_name = 'core/home.html'
