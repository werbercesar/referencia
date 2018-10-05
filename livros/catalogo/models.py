from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    pseudonimo = models.CharField(max_length=100, verbose_name="Pseudônimo ou Nome Universal", null=True, blank=True)
    data_nascimento = models.CharField(max_length=50, verbose_name="Data de nascimento", null=True, blank=True)
    local_nascimento = models.CharField(max_length=50, verbose_name="Local de nascimento", null=True, blank=True)
    data_obito = models.CharField(max_length=50 , verbose_name="Data do óbito", null=True, blank=True)
    local_obito = models.CharField(max_length=50, verbose_name="Local do óbito", null=True, blank=True)
    lingua_original = models.CharField(max_length=50, verbose_name="Línguas utilizadas", null=True, blank=True)

    def __str__(self): return self.nome + ' ' + self.sobrenome

    def chamada(self):
        # TODO Colocar esse método em um ModelManager de PapelPessoa
        pseudo = str()
        if self.pseudonimo: pseudo = ' (' + self.pseudonimo + ')'
        return self.sobrenome.upper() + ', ' + self.nome + pseudo


class Fonte(models.Model):
    # TODO """remote"""
    autor = models.ManyToManyField(Pessoa, verbose_name="Autoria", through="PapelPessoa")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo", null=True, blank=True)
    resumo = models.TextField(verbose_name="Resumo", null=True, blank=True)

    # TODO mover para um ModelManager da vida
    def autoria(self):
        n_tmp = ''
        for a in self.autor.all(): n_tmp += a.chamada() + '; '
        return n_tmp.strip()[:-1]


class Papel(models.Model):
    nome = models.CharField(max_length=25, verbose_name='Nome do papel')
    abreviatura = models.CharField(max_length=6, verbose_name='Abreviatura')
    autoridade_fonte = models.BooleanField(verbose_name="Este papel é de autoridade da fonte?", default=False)

class PapelPessoa(models.Model):
    papel  = models.ForeignKey(Papel, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    fonte  = models.ForeignKey(Fonte , on_delete=models.CASCADE)
    ordem  = models.PositiveSmallIntegerField(verbose_name="Ordem de citação")

class Livro(Fonte):
    edicao = models.CharField(max_length=10, verbose_name="Edição", null=True, blank=True)
    local = models.CharField(max_length=50, verbose_name="Local da publicação", null=True, blank=True)
    editora = models.CharField(max_length=50, verbose_name="Editora", null=True, blank=True)
    ano = models.CharField(max_length=50, verbose_name="Ano da publicação", null=True, blank=True)
    paginas = models.CharField(max_length=5 , verbose_name="Número de páginas", null=True, blank=True)
    colecao = models.CharField(max_length=50, verbose_name="Coleção", null=True, blank=True)
    volume = models.CharField(max_length=50, verbose_name="Volume", null=True, blank=True)

    def __str__(self): return self.titulo

    # TODO os métodos devem ir para um ModelManager
    def titulacao(self):
        str_titulo = self.titulo
        if self.subtitulo: str_titulo += ': ' + self.subtitulo
        return str_titulo

    def imprenta(self):
        return self.local + ': ' + self.editora + ', ' + self.ano

    def referencia(self):
        return self.autoria() + '. ' + self.titulacao() + '. ' + self.imprenta() + '.'