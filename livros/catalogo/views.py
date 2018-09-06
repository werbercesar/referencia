from django.shortcuts import render
# from django.views import generic

from . import models


def index(request):

    num_livros = models.Livro.objects.all().count()
    num_autores = models.Autor.objects.all().count()

    contexto = {
        'num_livros': num_livros,
        'num_autores': num_autores,
    }

    return render(request, "index.html", context=contexto)