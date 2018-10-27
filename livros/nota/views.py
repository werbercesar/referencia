from django.shortcuts import render
from .models import Etiqueta
from .tables import EtiquetaTable

def etiqueta_list(request):
    etiqueta_table = EtiquetaTable(Etiqueta.objects.all())
    return render(request, 'etiqueta_list.html', {'etiqueta_table': etiqueta_table})


