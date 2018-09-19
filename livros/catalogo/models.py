from django.db import models


class Pessoa(models.Model):
    nome       = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome  = models.CharField(max_length=100, verbose_name="Sobrenome")
    pseudonimo = models.CharField(max_length=100, verbose_name="Pseudônimo", null=True, blank=True)
    nascimento = models.CharField(max_length=50 , verbose_name="Nascimento", null=True, blank=True)
    obito      = models.CharField(max_length=50 , verbose_name="Morte"     , null=True, blank=True)
    local_nascimento = models.CharField(max_length=50, verbose_name="Local de nascimento", null=True, blank=True)
    lingua_original  = models.CharField(max_length=50, verbose_name="Línguas utilizadas" , null=True, blank=True)

    def __str__(self): return self.nome

    def chamada(self):
        # TODO Isso é assim mesmo? Talvez toda a hierarquia Pessoa < Autor ... etc deva ser revista: K.I.S.S
        pseudo = str()
        if self.pseudonimo: pseudo = ' (' + self.pseudonimo + ')'
        return self.sobrenome.upper() + ', ' + self.nome + pseudo


class Autor(Pessoa):
    magni_opera = models.CharField(max_length=200, verbose_name="Magni opera", null=True, blank=True)

class Organizador(Pessoa):
    def chamada(self):
        nome_chamada = super(Pessoa, self).chamada()
        return  nome_chamada + '(org.)'

class Fonte(models.Model):
    autor     = models.ManyToManyField(Autor   , verbose_name="Autoria")
    titulo    = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo", null=True, blank=True)
    resumo    = models.TextField(verbose_name="Resumo"                   , null=True, blank=True)

    def autoria(self):
        n_tmp = ''
        for a in self.autor.all(): n_tmp += a.chamada() + '; '
        return n_tmp.strip()[:-1]


class Livro(Fonte):
    edicao  = models.CharField(max_length=10, verbose_name="Edição"             , null=True, blank=True)
    local   = models.CharField(max_length=50, verbose_name="Local da publicação", null=True, blank=True)
    editora = models.CharField(max_length=50, verbose_name="Editora"            , null=True, blank=True)
    ano     = models.CharField(max_length=50, verbose_name="Ano da publicação"  , null=True, blank=True)
    paginas = models.CharField(max_length=5 , verbose_name="Número de páginas"  , null=True, blank=True)
    colecao = models.CharField(max_length=50, verbose_name="Coleção"            , null=True, blank=True)
    volume  = models.CharField(max_length=50, verbose_name="Volume"             , null=True, blank=True)

    def __str__(self): return self.titulo

    def titulacao(self):
        str_titulo = self.titulo
        if self.subtitulo: str_titulo += ': ' + self.subtitulo
        return str_titulo

    def imprenta(self):
        return self.local + ': ' + self.editora + ', ' + self.ano

    def referencia(self):
        return self.autoria() + '. ' + self.titulacao() + '. ' + self.imprenta() + '.'