from django.shortcuts import render
from django.views.generic import ListView
from . import models

def index(request):
    lista_fonte = models.Fonte.objects.all()
    lista_livro = models.Livro.objects.all()
    contexto = {
       "lista_fonte": lista_fonte,
       "lista_livro": lista_livro,
    }
    return render(request, "index.html", context=contexto)

class ListaFontes(ListView):
    model = models.Fonte
    context_object_name = 'lista_de_fontes'
    template_name = "lista_fontes.html"

