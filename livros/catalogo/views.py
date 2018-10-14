from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models


def index(request):
    lista_fonte = models.Fonte.objects.all()
    lista_livro = models.Livro.objects.all()
    contexto = {
        "lista_fonte": lista_fonte,
        "lista_livro": lista_livro,
    }
    return render(request, "index.html", context=contexto)

def papeis(request):
    lista_papeis = models.Papel.objects.all()
    campos = models.Papel._meta.get_fields()
    verbose = []
    for c in campos:
        if c.editable: verbose.append(c.verbose_name)
    # verbose = [c.verbose_name for c in campos]
    contexto = { "lista_papeis": lista_papeis,
                 "cabecalho": verbose,}
    return render(request, "papel/papel_list.html", context=contexto)

class ListaFontes(ListView):
    model = models.Fonte
    context_object_name = "lista_de_fontes"
    template_name = "lista_fontes.html"

class CreatePapel(CreateView):
    model = models.Papel
    fields = ['nome', 'abreviatura', 'autoridade_fonte']
    template_name = "papel_create.html"
