from django.test import TestCase
from util.util import UtilABNT


class TestUtil(TestCase):
    """
    Testes da classe UtilABNT
    """
    def test_nome_comum_bem_formatado(self):
        self.assertEquals('José', UtilABNT.nome_abnt(self, 'José Saramago'))

    def test_sobrenome_comum_bem_formatado(self):
        self.assertEquals('Saramago', UtilABNT.sobrenome_abnt(self, 'José Saramago'))

    def test_sobrenome_composto_bem_formado(self):
        self.assertEquals('Castelo Branco', UtilABNT.sobrenome_abnt(self, 'Camilo Castelo Branco', 2))

    def test_iniciais(self):
        self.assertEquals('J. A. S.', UtilABNT.iniciais_abnt(self, 'José Alceu Sampaio Correia'))

    def test_nome_com_espacos_extras(self):
        self.assertEquals('José', UtilABNT.nome_abnt(self, '   José    Saramago    '))

    def test_sobrenome_com_espacos_extras(self):
        self.assertEquals('Saramago', UtilABNT.sobrenome_abnt(self, '   José    Saramago    '))

    def test_iniciais_com_espacos_extra(self):
        self.assertEquals('J.', UtilABNT.iniciais_abnt(self, '   José    Saramago    '))
