from django.contrib import admin
from catalogo.models import Pessoa, Fonte, Papel, PapelPessoa, Livro


admin.site.register(Pessoa)
admin.site.register(Fonte)
admin.site.register(Papel)
admin.site.register(PapelPessoa)
admin.site.register(Livro)