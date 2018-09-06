from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome",
        help_text="O primeiro nome do autor. (ex.: 'Aurelius' em 'Aurelius Augustinus')")
    sobrenome = models.CharField(max_length=100, default='', verbose_name="Sobrenome",
        help_text="O sobrenome ou nome familiar do autor. (ex.: 'Augustinus' em 'Aurelius Augustinus')")
    pseudonimo = models.CharField(max_length=100, verbose_name="Pseudônimo",
        help_text="Pseudonimo ou nome universal do autor. (ex.: 'Santo Agostinho')")
    nascimento = models.CharField(max_length=50, verbose_name="Nascimento", null=True, blank=True,
        help_text="Data de nascimento ou aproximações. (ex.: '354 d.C.')")
    obito = models.CharField(max_length=50, verbose_name="Morte", null=True, blank=True,
        help_text="Data da morte ou aproximações. (ex.: '28/08/430')")
    local_nascimento = models.CharField(max_length=50, null=True, blank=True, verbose_name="Local de nascimento",
        help_text="Local de nascimento.Sempre atualizar. (ex.: Província romana de Hipona, atual Annaba na Argélia)")
    lingua_original = models.CharField(max_length=50, null=True, blank=True, verbose_name="Língua utilizadas",
        help_text="Línguas utilizadas pelo autor nas suas principais obras. (ex.: 'Latim')")
    magni_opera = models.CharField(max_length=200, verbose_name="Magni opera", null=True, blank=True,
        help_text="Lista das maiores obras do autor (ex.: 'A cidade de Deus, Confissões')")

    def __str__(self): return self.nome

    ### business logic methods
    def chamada(self):
        pseudo = ''
        if len(self.pseudonimo.strip()) > 0:
            pseudo = ' (' + self.pseudonimo + ')'
        return self.sobrenome.upper() + ', ' + self.nome + pseudo


class Livro(models.Model):
    autor = models.ManyToManyField(Autor, verbose_name="Autoria",
        help_text="Indique o autor ou autores da obra")
    titulo = models.CharField(max_length=200, verbose_name="Título",
        help_text="Titulo do livro (ex.: 'Confissões')")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo", default='', null=True, blank=True,
        help_text="Subtitulo do livro")
    edicao = models.CharField(max_length=10, verbose_name="Edição", null=True, blank=True,
        help_text="Número da edição (utilizar número arábico e preencher mesmo que seja a primeira edição)")
    local = models.CharField(max_length=50, verbose_name="Local da publicação", null=True, blank=True,
        help_text="Informe o local da publicação. (ex.: 'Rio de Janeiro', 'Patos-PB')")
    editora = models.CharField(max_length=50, verbose_name="Editora", null=True, blank=True,
        help_text="Informe o nome da editora. (ex.: 'Cultrix')")
    ano = models.CharField(max_length=50, verbose_name="Ano da publicação", null=True, blank=True,
        help_text="O ano da publicação, quando disponível (ex.: '1973', '198?' '1600?')")
    paginas = models.CharField(max_length=5, verbose_name="Número de páginas", null=True, blank=True,
        help_text="O número de páginas do livros. (consulte sempre a imprenta)")
    colecao = models.CharField(max_length=50, verbose_name="Coleção", null=True, blank=True,
        help_text="Indique o noem da coleção, se houver. (ex.: 'Primeiros passos', 'O que é?')")
    volume = models.CharField(max_length=50, verbose_name="Volume", null=True, blank=True,
        help_text="Indique o número do volume, se houver mais de um (ex.: 'Volume 9')")
    sumario = models.TextField(max_length=1500, verbose_name="Sumário", null=True, blank=True,
        help_text="Breve descrição do conteúdo da obra (até 1500 caracteres).")

    def __str__(self): return self.titulo

    def autoria(self):
        return Autor.chamada(self.autor)

    def titulacao(self):
        str_titulo = self.titulo
        if len(self.subtitulo.strip()) > 0:
            str_titulo = str_titulo + ': ' + self.subtitulo
        return str_titulo + '.'

    def imprenta(self):
        return self.local + ':' + self.editora + ', ' + self.ano

    def referencia(self):
        return self.autoria() + self.titulacao() + self.imprenta()





