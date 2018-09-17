from django.db import models


class Etiqueta(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Etiqueta",
        help_text="Uma etiqueta para classificação/marcação da anotação. (ex.: 'Segunda Guerra', 'Xadrez')")

    cor = models.CharField(max_length=6, verbose_name="Cor", default='6A5ACD',
        help_text="A cor da etiqueta por ajudá-lo na classificação de suas anotações (use com sabedoria...)")


class Anotacao(models.Model):
    tag = models.ManyToManyField(Etiqueta, verbose_name="Etiqueta",
        help_text="Marque suas anotações para recuperá-las facilmente depois")

    data = models.DateField(verbose_name="Data da criação", auto_now_add=True,
        help_text="Saber a data da criação da anotação ajudará a organizar seus trabalhos")

    texto = models.TextField(verbose_name="Anotação",
        help_text="Sua anotação vai aqui")

