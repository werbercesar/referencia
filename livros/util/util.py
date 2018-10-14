"""
classes e funções utilitárias comuns aos aplicativos
"""
import re
#from django.db import models


# class TabelaDeDados():
#
#     def __init__(self, dados, cabecalho=True, rodape=False, editar='#', excluir='#'):
#
#         _dados = dados.objects.all()
#         _campos = dados._meta.get_fields()
#         lista_campos = [campo.name for campo in _campos if campo.editable]
#         lista_cabecalho = [cabec.verbose_name for cabec in _campos if cabec.editable]
#         string_output = "<table> "
#         if cabecalho:
#             string_output += " <thead> <tr> "
#             for cb in lista_cabecalho:
#                 string_output += "<th>" + cb + "</th> "
#         string_output += "<th>Editar</th> <th>Excluir</th> </tr> </thead> <tbody> <tr>"
#
#         for d in lista_dados:
#
#                 <td>{{ papel.id }}</td>
#                 <td>{{ papel.nome }}</td>
#                 <td>{{ papel.abreviatura }}</td>
#                 <td>{{ papel.autoridade_fonte }}</td>
#                 <td><a href="#"><span class="material-icons">edit</span></a></td>
#                 <td><a href="#"><span class="material-icons">delete</span></a></td>
#             </tr>
#         {% endfor %}
#         </tbody>
#     </table>
# "
