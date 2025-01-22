import unittest
from src.negocio.ContaPoupanca import ContaPoupanca  # Importe sua classe corretamente
class TestContaPoupanca(unittest.TestCase):    
    def setUp(self):
        """
        Método executado antes de cada teste.
        Cria uma instância de ContaPoupanca para ser usada nos testes.
        """
        self.conta = ContaPoupanca(numero="12345", saldo=1000.0)
        self.conta2 = ContaPoupanca(numero="123454", saldo=900.0)  
    def test_criacao_conta(self):
        """
        Testa se a conta é criada com o saldo e número corretos.
        """
        self.assertEqual(self.conta.getSaldo(), 1000.0)
        self.assertEqual(self.conta.getNumero(), "12345")  # Verifica o número da conta
    def test_render_juros(self):
        """
        Testa o método render_juros.
        Aplica uma taxa de 5% (0.05) e verifica o saldo atualizado.
        """
        self.conta.render_juros(0.05)  # Aplica juros de 5%
        self.assertEqual(self.conta.getSaldo(), 1050.0)  # Novo saldo deve ser 1050.0
    def test_get_tipo(self):        """
        Testa o método get_tipo.
        """
        self.assertEqual(self.conta.get_tipo(), "poupanca")  # Deve retornar "poupanca"
if __name__ == "__main__":
    unittest.main()