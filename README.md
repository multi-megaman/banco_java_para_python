
## Instalação de dependências e preparação do ambiente
OBS: é necessário o python **3.12+**

O primeiro e único passo para preparar o projeto é instalar as dependências e configurar o projeto, para isto, basta abrir o terminal e rodar os seguintes comandos:

```bash
$ pip install -f pasta/raiz/do/projeto/requirements.txt
$ pip install -e pasta/raiz/do/projeto
```

Ou se você já abriu um terminal da pasta raiz:

```bash
$ pip install -r requirements.txt
$ pip install -e .
```


Com isso, o projeto já deve estar completamente funcional. Para testar e utilizar o sistema bancário, basta rodar o arquivo "app.py" na raiz do projeto e uma interface deve ser exibida:


```bash
$ python app.py
```

## Para executar testes unitários

Os conjuntos de testes unitários podem ser rodados separadamente para cada classe dentro da pasta "test" na raiz desse projeto. Os testes unitários são feitos com o unittest (equivalente ao JUnit do Java) e, ao rodar algum dos arquivos .py de teste, um retorno será dado no terminal indicando os sucessos, falhas e erros de cada teste. Também é possível rodar todos os testes unitários de todas as classes de uma só vez rodando o arquivo "tudo_test.py" dentro da pasta "test"

Exemplo de teste unitário da classe conta rodando pelo terminal:

```bash
$ python test/conta_test.py
```

o retorno no próprio terminal deve ser algo do tipo:

```bash
test_conta_debito (__main__.test_conta_debito.test_conta_debito) ... ok
test_conta_debito_saldo_insuficiente (__main__.test_conta_debito_saldo_insuficiente.test_conta_debito_saldo_insuficiente) ... ok
test_conta_numero (__main__.test_conta_numero.test_conta_numero) ... ok
test_conta_saldo_inicial_negativo (__main__.test_conta_saldo_inicial_negativo.test_conta_saldo_inicial_negativo) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

Erros e problemas comuns:

Em linux, pode ocorrer de surgir um problema relacionado ao "Tkinter". Muito provavelmente significa que o Tkinter não está devidamente instalado no linux.

```bash
$ sudo apt-get install python3-tk
```

se esse comando não funcionar, tente o comando abaixo  (créditos: plmorais):

```bash
sudo apt install build-essential libbz2-dev libssl-dev zlib1g-dev libffi-dev libreadline-dev libsqlite3-dev tk-dev -y
```


## Para ver a cobertura de linhas ou de branches dos testes

Será necessário utilizar a biblioteca Coverage para saber o percentual de linhas cobertas ou de decisões totalmente cobertas.
Para ilustrar a utilização do coverage, vamos utilizar o arquivo de teste "conta_imposto_test.py" como exemplo.
Ao invés de rodar o teste normalmente, por exemplo, com o comando "python test/conta_imposto_test.py" utilizaremos o coverage da seguinte forma:

```bash
python -m coverage run ./test/conta_imposto_test.py
```

Isso fará com que o coverage rode o mesmo teste, porém agora tomando nota das informações de cobertura de linhas. Para melhor visualizar as informações coletadas nos testes, rode o comando:

```bash
python -m coverage html
```

Com isso, uma nova pasta deve ser criada no diretório raiz do seu projeto chamada "htmlcov" ou algo similar e dentro dela você deve abrir o arquivo "index.html"; nele estarão as informações de 
porcentagem de cobertura de linhas de cada arquivo que foi utilizado no teste rodado.

Esse processo serve para ver a cobertura de linhas, porém para ver a cobertura de branches, rode os seguintes comandos:

```bash
python -m coverage run --branch ./test/conta_imposto_test.py
python -m coverage html
```

Com isso, o html deve incluir as porcentagens de cobertura de branches.



