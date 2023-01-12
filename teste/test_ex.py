import unittest

def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f'{value} deve ser do tipo cadeia de caracteres(string)')
    true_values = ['s', 'sim']
    false_values = ['não', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False


class TestStrToBoll(unittest.TestCase):
    def test_y_true(self):
        resultado = str_to_bool('s')
        self.assertTrue(resultado)
    
    def test_yes_true(self):
        resultado = str_to_bool('sim')
        self.assertTrue(resultado)

    def test_input_invalido(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1) 


# principal
if __name__=='__main__':
    unittest.main()

'''
    Código herdado
Uma maneira de pensar no código não testado é rotulá-lo como herdado. É comum encontrar código não testado em projetos de software. O código pode deixar de ser testado por diferentes motivos, como falta de experiência com testes ou práticas de desenvolvimento que não permitem tempo suficiente para considerar o teste como parte da produção de software.

Como já mencionado, uma característica do código não testado é que é difícil de compreender e muitas vezes pode ser bastante complexo pelo mesmo motivo. Um efeito colateral de todos esses problemas é que torna o código ainda mais difícil de lidar, fazendo com que a função (ou método) continue aumentando com mais lógica e caminhos de código mais entrelaçados.

Quanto menor a função, mais fácil será testar.

    Ferramentas de teste
Alguns dos desafios vêm da falta de testes, enquanto outros estão relacionados a experiências ruins de teste e não saber quais técnicas aplicar. Já mencionamos o código herdado neste módulo e como o código não testado pode continuar aumentando de tamanho e complexidade. As ferramentas de cobertura de teste podem informar com precisão quais caminhos de código são testados e quais não estão sendo cobertos por testes existentes.

Contar com ferramentas e bibliotecas de teste é uma ótima maneira de reduzir a quantidade de esforço necessária para produzir bons testes. Dependendo da linguagem e do aplicativo que está sendo testado, você deve encontrar soluções que possam tornar os testes mais fáceis e robustos.

Aqui estão alguns exemplos sobre o que essas ferramentas devem ser:

Uma ferramenta de cobertura de teste para relatar caminhos de código testados e não testados.
Uma ferramenta de execução de testes, que pode coletar, executar e executar novamente testes específicos.
Um ambiente CI/CD, que pode executar testes automaticamente e evitar que código defeituoso seja mesclado ou implantado.
'''
