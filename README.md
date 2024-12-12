
## Instalação de dependências e preparação do ambiente
OBS: é necessário o python **3.12+**

O primeiro e único passo para preparar o projeto é instalar as dependências e configurar o projeto, para isto, basta abrir o terminal e digitar:

```bash
$ pip install -e pasta/raiz/do/projeto
```

Ou se você já abriu um terminal da pasta raiz:

```bash
$ pip install -e .
```


Com isso o projeto já deve estar completamente funcional. Para testar e utilizar o sistema bancário, basta rodar o arquivo "app.py" na raiz do projeto e uma interface deve ser exibida:

```bash
$ python app.py
```

## Para executar testes unitários

Os conjuntos de testes unitários podem ser rodados separadamente para cada classe dentro da pasta "test" na raiz desse projeto. Os testes unitários são feitos com o unittest (equivalente ao JUnit do Java) e, ao rodar algum dos arquivos .py de teste, um retorno será dado no terminal indicando os sucessos, falhas e erros de cada teste. Também é possível rodar todos os testes unitários de todas as classes de uma só vez rodando o arquivo "tudo_test.py" dentro da pasta "test"

Exemplo de teste unitário da classe conta rodando pelo terminal:

```bash
$ python test/conta_test.py
```

o retorno no proprio terminal deve ser algo do tipo:

```bash
test_conta_debito (__main__.test_conta_debito.test_conta_debito) ... ok
test_conta_debito_saldo_insuficiente (__main__.test_conta_debito_saldo_insuficiente.test_conta_debito_saldo_insuficiente) ... ok
test_conta_numero (__main__.test_conta_numero.test_conta_numero) ... ok
test_conta_saldo_inicial_negativo (__main__.test_conta_saldo_inicial_negativo.test_conta_saldo_inicial_negativo) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
