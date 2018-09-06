from django.db import models


class Etiqueta(models.Model):
    nome = models.CharField(
        max_length=50,
        help_text="Uma etiqueta para classificação/marcação da anotação. (ex.: 'Segunda Guerra', 'Xadrez')",
        verbose_name="Etiqueta"
    )


class Anotacao(models.Model):
    tag = models.ManyToManyField(
        Etiqueta,
        help_text="Marque suas anotações para recuperá-las facilmente depois",
        verbose_name="Etiqueta"
    )
    data = models.DateField(

    )

