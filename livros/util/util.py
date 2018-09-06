"""
classes e funções utilitárias comuns aos aplicativos
"""
import re


class UtilABNT:
    NOME = 'nome'
    SOBRENOME = 'sobrenome'
    INICIAIS = 'iniciais'

    conectivos = ['a', 'e', 'i', 'y', 'o', 'da', 'das', 'de', 'do', 'dos', 'y', 'zur', 'von']

    def decompoe_nome(self, nome_registrado, num_sobrenomes=1):
        """
        Decompõe o nome do autor em nome e sobrenome. Normalmente, o sobrenome é a última cadeia de caracteres,
        mas há a possibilidade de ser composto e não hifenizado ou ser seguido de indicativo de relação familiar.
        Esses casos são tratados na função de acordo com a norma ABNT XXXX.
        Ex. 1: Filho é indicativo familiar. Em "João Manoel de Sousa Filho" "Sousa Filho" é o sobrenome.
        Ex. 2: Castelo Branco é composto sem hífen. Em "Antonio Castelo Branco" "Castelo Branco" é o sobrenome.
        Ex. 3: Em "Antonio Castelo Branco Filho" o sobrenome a ser extraído é "Castelo Branco Filho"
        O sobrenome deve aparecer em maiúsculas na lista de referências, mas há outras ocasiões em que pode ser
        desejável tê-lo em minúsculas. Fica a cargo do usuário a melhor forma de apresentação.
        Por fim, como saber se um sobrenome é composto ou não ou como saber se a última cadeia de caracteres é um
        indicativo de relação familiar? Teríamos que mapear em listas exaustivas (e em várias línguas),
        pois não existe uma regra determinística para computar a questão. Optamos então por indicar
        a quantidade de cadeias que devem ser consideradas como sobrenomes pois isso simplifica a questão e também
        facilita a obtenção do sobrenome em línguas estrangeiras

        O nome é o que sobra após a extração do sobrenome. Há duas formas de livre escolha para apresentação do
        nome na ABNT: nome por extenso e apenas as iniciais seguidas de ponto. A função fornece ambos os formatos.
        Ex. 4: "Antonio Carlos Castelo Branco" => "Antonio Carlos" e "A. C."

        :param nome_registrado: Um string com o nome natural do autor. Ex.: "Antonio Carlos Castelo Branco". Normalmente,
        o nome deveria ser vir no formato final, mas pode acontecer de serem incluidos espaços extras desnecessários e isso não
        ter sido adequadamente tratado no nível de banco de dados; como os nomes na formatação ABNT não possuem espaços
        duplicados ou espaços antes e depois, esse aspecto foi tratado na função.
        Ex. 5: "...João..Pessoa.." será alterado para "João.Pessoa" (Neste exemplo os espaços em branco foram trocados
        por pontos para melhor visualização)
        :param num_sobrenomes: Indica a quantidade sobrenomes a ser extraída do nome completo. o valor default é 1
        :return: Um dicionário com as chaves NOME, SOBRENOME e INICIAIS.
        """
        # purga simultaneamente espaços iniciais, finais e duplicados
        nome_purgado = re.sub(' +', ' ', nome_registrado).strip(' ')

        # agora é seguro dividir o nome em itens de uma lista usando o espaço em branco como separador
        # e extrair nome e sobrenome conforme o parâmetro (1 é o default)
        lista = nome_purgado.split(' ')
        nome = ' '.join(lista[:-num_sobrenomes])
        sobrenome = ' '.join(lista[-num_sobrenomes:])
        lista_iniciais = [l[0] for l in lista[:-num_sobrenomes]]
        iniciais = '. '.join(lista_iniciais)
        iniciais = iniciais + '.'
        
        ret = {UtilABNT.NOME: nome, UtilABNT.SOBRENOME: sobrenome, UtilABNT.INICIAIS: iniciais}
        return ret

    # @staticmethod
    def nome_abnt(self, nome, num_sobrenomes=1):
        return UtilABNT.decompoe_nome(self, nome, num_sobrenomes)[UtilABNT.NOME]

    # @staticmethod
    def sobrenome_abnt(self, nome, num_sobrenomes=1):
        return UtilABNT.decompoe_nome(self, nome, num_sobrenomes)[UtilABNT.SOBRENOME]

    def iniciais_abnt(self, nome, num_sobrenomes=1):
        return UtilABNT.decompoe_nome(self, nome, num_sobrenomes)[UtilABNT.INICIAIS]

    def nome_autor_chamada(self, nome, iniciais=True):
        """
        Retorna o nome do autor no formato esperado pelo sistema Autor-Data.
        :param nome: O nome natural do autor
        :param iniciais: Indica se a função deve retornar as iniciais ou o string completo do nome. Default é True
        :return: O "SOBRENOME, nome" do autor. Ex.: 'Franz Kafka' => 'KAFKA, Franz' ou 'KAFKA, F.'
        """
        if iniciais:
            n = self.iniciais_abnt(nome).upper()
        else:
            n = self.sobrenome_abnt(nome)
        s = self.sobrenome_abnt(nome)
        return f'{s.upper()}, {n}'
