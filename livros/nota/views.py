from django.shortcuts import render

def manage_anotacao(request, caderno_id):

    caderno = get_object_or_404(models.Caderno)