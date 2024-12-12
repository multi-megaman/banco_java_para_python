from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB
from src.negocio.Cliente import Cliente
from src.negocio.ContaAbstrata import ContaAbstrata
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca
from src.exceptions import RenderJurosPoupancaException
from src.exceptions.AtualizacaoNaoRealizadaException import AtualizacaoNaoRealizadaException
from src.exceptions.ClienteJaCadastradoException import ClienteJaCadastradoException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.ContaJaAssociadaException import ContaJaAssociadaException
from src.exceptions.ContaJaCadastradaException import ContaJaCadastradaException
from src.exceptions.ContaNaoEncontradaException import ContaNaoEncontradaException
from src.exceptions.RenderBonusContaEspecialException import RenderBonusContaEspecialException
from src.exceptions.ValorInvalidoException import ValorInvalidoException


class Banco:

    instance = None

    def __init__(self, clientes: RepositorioClientesArquivoDB, contas: RepositorioContasArquivoDB):
        self.clientes = clientes
        self.contas = contas

    @classmethod
    def get_instance(cls) -> 'Banco':
        if cls.instance is None:
            cls.instance = Banco(RepositorioClientesArquivoDB, RepositorioContasArquivoDB)
        return cls.instance

    def cadastrar_cliente(self, cliente: Cliente):
        if not self.clientes.inserir(cliente):
            raise ClienteJaCadastradoException()

    def procurar_cliente(self, cpf: str) -> Cliente:
        return self.clientes.procurar(cpf)

    def cadastrar_conta(self, conta: ContaAbstrata):
        if not self.contas.inserir(conta):
            raise ContaJaCadastradaException()

    def procurar_conta(self, numero: str) -> ContaAbstrata:
        return self.contas.procurar(numero)

    def associar_conta(self, cpf: str, numero_conta: str):
        cliente = self.procurar_cliente(cpf)
        if cliente:
            conta = self.procurar_conta(numero_conta)
            if conta is None:
                cliente.adicionar_conta(numero_conta)
                self.clientes.atualizar(cliente)
            else:
                raise ContaJaAssociadaException()
        else:
            raise ClienteNaoCadastradoException()

    def remover_cliente(self, cpf: str):
            cliente = self.procurar_cliente(cpf)
            i = 0
            while cliente.contas:
                numero_conta = cliente.consultar_numero_conta(i)
                i += 1
                self.remover_conta(cliente, numero_conta)
            if not self.clientes.remover(cpf):
                raise ClienteNaoCadastradoException()

    def remover_conta(self, cliente: Cliente, numero_conta: str):
        cliente.remover_conta(numero_conta)
        if not self.contas.remover(numero_conta):
            raise ContaNaoEncontradaException()
        self.clientes.atualizar(cliente)

    def creditar(self, conta: ContaAbstrata, valor: float):
        if valor < 0:
            raise ValorInvalidoException()
        conta.creditar(valor)
        self.contas.atualizar(conta)

    def debitar(self, conta: ContaAbstrata, valor: float):
        if valor < 0:
            raise ValorInvalidoException()
        if self.contas.existe(conta.getNumero()):
            conta.debitar(valor)
            self.contas.atualizar(conta)

    def transferir(self, conta_origem: ContaAbstrata, conta_destino: ContaAbstrata, valor: float):
        if self.contas.existe(conta_origem.getNumero()) and self.contas.existe(conta_destino.getNumero()):
            self.debitar(conta_origem, valor)
            self.creditar(conta_destino, valor)
            self.contas.atualizar(conta_origem)
            self.contas.atualizar(conta_destino)

    def atualizar_cliente(self, cliente: Cliente):
        if not self.clientes.atualizar(cliente):
            raise AtualizacaoNaoRealizadaException()

    def render_bonus(self, conta: ContaAbstrata):
        if isinstance(conta, ContaEspecial):
            if self.contas.existe(conta.getNumero()):
                conta.render_bonus()
                self.contas.atualizar(conta)
            else:
                raise ContaNaoEncontradaException()
        else:
            raise RenderBonusContaEspecialException()

    def render_juros(self, conta: ContaAbstrata):
        if isinstance(conta, ContaPoupanca):
            if self.contas.existe(conta.getNumero()):
                conta.render_juros(0.5)
                self.contas.atualizar(conta)
            else:
                raise ContaNaoEncontradaException()
        else:
            raise RenderJurosPoupancaException()
