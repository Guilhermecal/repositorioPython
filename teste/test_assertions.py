"""
Testes com Python
o python tem um módulo de teste chamado unittest em sua biblioteca padrão, portanto não há necessidade de baixar e instalar.

Classes e herança são a base para usar unittest para gravar testes. Portanto não é possivel gravar funções de teste ou outros testes que não usem a classe base do unttest.
"""

import unittest
class TestAssertions(unittest.TestCase):# nomes de metodos de teste sempre começaram com a palavra teste
    def test_eq(self):
        # testa se a cadeia de caracteres são iguais
        a = 'Gsc'
        b = 'Gsc'
        self.assertEqual(a, b)


'''
class TestContas(unittest.TestCase):
    def test_criar(self):
        self.account = bool
        self.assertTrue(account.create())

    def test_deletar(self):
        self.assertTrue(account.delete())
'''
# permite executar os testes executando o arquivo com o Python
if __name__== '__main__':
    unittest.main()