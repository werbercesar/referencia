import django_tables2 as tables
from .models import Etiqueta


class EtiquetaTable(tables.Table):
    class Meta:
        model = Etiqueta
