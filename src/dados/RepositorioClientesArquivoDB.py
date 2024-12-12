import sqlite3
import json

from src.dados.IRepositorioClientes import IRepositorioClientes
from src.negocio.Cliente import Cliente

class RepositorioClientesArquivoDB(IRepositorioClientes):
    def __init__(self, db_path="clientes.db"):
        """
        Inicializa o repositório, conectando-se ao banco de dados SQLite.
        Cria a tabela de clientes se ela não existir.
        """
        self.db_path = db_path
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    cpf TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    contas TEXT
                )
            """)

    def _connect(self):
        """
        Cria uma conexão com o banco de dados.
        """
        return sqlite3.connect(self.db_path)

    def inserir(self, cliente: Cliente) -> bool:
        """
        Insere um novo cliente no banco de dados.
        :param cliente: Cliente a ser inserido.
        :return: True se inserido com sucesso, False se ocorrer erro.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes (cpf, nome, contas)
                    VALUES (?, ?, ?)
                """, (cliente.get_cpf(), cliente.get_nome(), json.dumps(cliente.get_contas())))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False

    def procurar(self, cpf: str) -> Cliente:
        """
        Procura um cliente pelo CPF.
        :param cpf: CPF do cliente.
        :return: Cliente ou None se não encontrado.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
            row = cursor.fetchone()
            if row:
                cliente = Cliente(row[1], row[0])
                contas = json.loads(row[2])
                for conta in contas:
                    cliente.adicionar_conta(conta)
                return cliente
            return None

    def remover(self, cpf: str) -> bool:
        """
        Remove um cliente pelo CPF.
        :param cpf: CPF do cliente.
        :return: True se removido com sucesso, False se não encontrado.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
            conn.commit()
            return cursor.rowcount > 0

    def atualizar(self, cliente: Cliente) -> bool:
        """
        Atualiza os dados de um cliente.
        :param cliente: Cliente com os dados atualizados.
        :return: True se atualizado com sucesso, False se não encontrado.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE clientes
                SET nome = ?, contas = ?
                WHERE cpf = ?
            """, (cliente.get_nome(), json.dumps(cliente.get_contas()), cliente.get_cpf()))
            conn.commit()
            return cursor.rowcount > 0

    def existe(self, cpf: str) -> bool:
        """
        Verifica se um cliente existe pelo CPF.
        :param cpf: CPF do cliente.
        :return: True se o cliente existe, False caso contrário.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM clientes WHERE cpf = ?", (cpf,))
            return cursor.fetchone() is not None

    def listar_clientes(self):
        """
        Lista todos os clientes no banco de dados.
        :return: Lista de dicionários com os dados dos clientes.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            return [{'cpf': row[0], 'nome': row[1], 'contas': json.loads(row[2])} for row in rows]


# Exemplo de uso
if __name__ == "__main__":
    repo = RepositorioClientesArquivoDB()

    # Inserir cliente
    cliente = Cliente("João da Silva", "12345678900")
    cliente.set_contas(["123", "456"])
    if repo.inserir(cliente):
        print("Cliente inserido com sucesso.")
    else:
        print("Cliente já cadastrado.")

    # Procurar cliente
    encontrado = repo.procurar("12345678900")
    if encontrado:
        print("Cliente encontrado:", encontrado.get_nome(), encontrado.get_contas())
    else:
        print("Cliente não encontrado.")

    # Atualizar cliente
    cliente_atualizado = Cliente("João Atualizado", "12345678900")
    cliente_atualizado.set_contas(["789", "101"])
    if repo.atualizar(cliente_atualizado):
        print("Cliente atualizado com sucesso.")
    else:
        print("Erro ao atualizar cliente.")

    # Remover cliente
    if repo.remover("12345678900"):
        print("Cliente removido com sucesso.")
    else:
        print("Cliente não encontrado para remoção.")

    # Listar clientes
    print("Lista de clientes:", repo.listar_clientes())