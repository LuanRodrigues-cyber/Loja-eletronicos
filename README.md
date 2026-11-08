# LOJA DE ELETRÔNICOS
### Sistema de gerenciamento de produtos, clientes, estoque e vendas

## 1. Apresentação do projeto

O projeto **Loja de Eletrônicos** foi desenvolvido utilizando a linguagem Python 3 como atividade acadêmica, com o objetivo de aplicar os conceitos de programação estruturada, modularização e programação orientada a objetos (POO).

O sistema simula o funcionamento básico de uma loja de produtos eletrônicos, permitindo o cadastro e a consulta de produtos e clientes, o gerenciamento de estoque, a realização de vendas e o armazenamento do histórico de compras de cada cliente.

O desenvolvimento foi realizado com a divisão do código em módulos, facilitando a organização, a manutenção e a compreensão das funcionalidades.

## 2. Objetivos do sistema

O principal objetivo é desenvolver um sistema que facilite o controle das operações básicas de uma loja de eletrônicos.

Entre os objetivos específicos estão:

- Organizar o cadastro de produtos e clientes.
- Controlar a quantidade de produtos disponíveis no estoque.
- Permitir a inclusão de novas unidades no estoque.
- Realizar vendas de produtos cadastrados.
- Calcular automaticamente o valor total de cada venda.
- Atualizar o estoque após a realização de uma venda.
- Impedir vendas com quantidades superiores ao estoque disponível.
- Armazenar e consultar o histórico de compras dos clientes.

## 3. Organização dos arquivos

O projeto está dividido em três arquivos principais, cada um responsável por uma parte específica do sistema.

### 3.1. main.py

O arquivo `main.py` é responsável pela execução principal do programa. Nele estão concentradas as funções que controlam as operações da loja, além do menu principal e dos submenus.

As principais funções implementadas são:

**cadastrar_produtos()**

Responsável por cadastrar novos produtos. Solicita ao usuário a marca, o preço e a quantidade inicial em estoque.

O código realiza verificações para impedir o cadastro com marca vazia, preço inválido ou estoque negativo. Após a validação, cria um objeto da classe `Eletronicos` e adiciona esse objeto à lista de produtos.

**incluir_estoque()**

Permite adicionar novas unidades a um produto já cadastrado.

A função percorre a lista de produtos para localizar a marca informada pelo usuário. Quando encontra o produto, solicita a quantidade que será adicionada e utiliza o método `adicionar_estoque()` para atualizar seu estoque.

**mostrar_produtos()**

Percorre a lista de produtos cadastrados e apresenta as informações de cada um, incluindo marca, preço e quantidade disponível em estoque.

Também verifica se existem produtos cadastrados antes de realizar a consulta.

**cadastrar_clientes()**

Responsável pelo cadastro de novos clientes. Solicita nome, CPF e endereço.

Antes de criar o objeto, verifica se os campos foram preenchidos e se o CPF informado já está cadastrado, evitando registros duplicados.

**mostrar_cliente()**

Percorre a lista de clientes e apresenta os dados de cada cliente cadastrado, incluindo nome, CPF e endereço.

**vendas()**

É uma das principais funções do sistema, pois reúne as operações necessárias para realizar uma venda.

Seu funcionamento ocorre em etapas:

1. Verifica se existem produtos e clientes cadastrados.
2. Solicita o CPF do cliente e verifica se ele existe.
3. Solicita a marca do produto e verifica se ele está cadastrado.
4. Verifica se existe estoque disponível.
5. Solicita a quantidade que será vendida.
6. Verifica se a quantidade solicitada é positiva e se não ultrapassa o estoque disponível.
7. Atualiza o estoque utilizando o método `remover_estoque()`.
8. Calcula o valor total da venda multiplicando o preço pela quantidade.
9. Registra a compra no histórico do cliente utilizando o método `registrar_compra()`.

Caso a quantidade solicitada seja superior ao estoque disponível, o sistema informa o usuário e permite informar uma quantidade menor.

**mostrar_compras()**

Responsável por consultar o histórico de compras dos clientes.

A função percorre a lista de clientes e verifica se cada um possui compras registradas. Quando existem compras, apresenta o produto, a quantidade adquirida e o valor total de cada operação.

### 3.2. produtos.py

O arquivo `produtos.py` contém a classe `Eletronicos`, responsável pela representação dos produtos cadastrados na loja.

**Classe Eletronicos**

A classe utiliza o método construtor `__init__()` para inicializar os objetos com três atributos:

- `marca`: armazena a marca do produto.
- `preco`: armazena o preço do produto.
- `estoque`: armazena a quantidade disponível.

**Métodos da classe**

`adicionar_estoque(quantidade)`

Recebe uma quantidade e adiciona esse valor ao estoque atual do produto.

`remover_estoque(quantidade)`

Recebe uma quantidade e subtrai esse valor do estoque atual do produto.

**Lista lista_produtos**

O módulo também possui a lista `lista_produtos`, utilizada para armazenar os objetos criados a partir da classe `Eletronicos`.

Essa lista permite que as demais funções do sistema acessem e manipulem os produtos cadastrados.

### 3.3. clientes.py

O arquivo `clientes.py` contém a classe `Cliente`, responsável por representar os clientes cadastrados na loja.

**Classe Cliente**

O método construtor `__init__()` inicializa os objetos com os seguintes atributos:

- `nome`: armazena o nome do cliente.
- `cpf`: armazena o CPF do cliente.
- `endereco`: armazena o endereço do cliente.
- `compras`: cria uma lista individual para armazenar o histórico de compras daquele cliente.

**Método da classe**

`registrar_compra(produto, quantidade, valor_total)`

Recebe as informações de uma venda e utiliza o método `append()` para adicionar um dicionário à lista `compras` do cliente.

Esse dicionário armazena três informações:

- Produto comprado.
- Quantidade adquirida.
- Valor total da compra.

**Lista lista_cliente**

O módulo possui a lista `lista_cliente`, responsável por armazenar os objetos criados a partir da classe `Cliente`.

Dessa maneira, o sistema consegue localizar os clientes e acessar seus respectivos históricos de compras.

## 4. Comunicação entre os módulos

Para permitir que os arquivos compartilhem informações e funcionalidades, foi utilizada a importação de módulos no arquivo principal:

```python
import produtos
import clientes
```

Com isso, o `main.py` consegue acessar as classes e listas presentes nos outros arquivos.

Por exemplo:

```python
item = produtos.Eletronicos(marca, preco, estoque)
produtos.lista_produtos.append(item)
```

Nesse trecho, um objeto da classe `Eletronicos` é criado e armazenado na lista de produtos.

Outro exemplo é o registro de uma compra:

```python
cliente_encontrado.registrar_compra(
    produto_encontrado.marca,
    quantidade,
    total
)
```

Nesse caso, o método da classe `Cliente` é utilizado para armazenar as informações da venda no histórico do cliente.

## 5. Conceitos de programação utilizados

Durante o desenvolvimento do projeto, foram aplicados os seguintes conceitos estudados em Python:

**Programação estruturada:** utilização de funções, estruturas condicionais e estruturas de repetição para organizar a lógica do sistema.

**Modularização:** divisão do programa em arquivos independentes, permitindo separar as responsabilidades de produtos, clientes e operações principais.

**Programação orientada a objetos (POO):** criação das classes `Eletronicos` e `Cliente`, utilizadas para representar os elementos principais do sistema.

**Classes e objetos:** criação de modelos e instâncias para armazenar e manipular os dados dos produtos e clientes.

**Atributos e métodos:** utilização de atributos para armazenar informações e métodos para executar operações relacionadas aos objetos.

**Listas:** armazenamento dos produtos, clientes e históricos de compras.

**Dicionários:** organização das informações de cada compra registrada no histórico do cliente.

**Estruturas condicionais:** utilização de `if`, `elif` e `else` para verificar condições e controlar as decisões do programa.

**Estruturas de repetição:** utilização de `while` e `for` para repetir operações, percorrer listas e permitir novas tentativas de entrada.

**Tratamento de exceções:** utilização de `try` e `except` para tratar erros de conversão de valores numéricos, evitando que entradas inválidas interrompam o funcionamento do sistema.

## 6. Validações e tratamento de situações inválidas

Para melhorar o funcionamento do sistema, foram implementadas algumas verificações:

- Impedir o cadastro de produtos com campos vazios.
- Impedir preços iguais ou inferiores a zero.
- Impedir o cadastro de produtos com estoque negativo.
- Impedir o cadastro de clientes com informações vazias.
- Evitar o cadastro de clientes com CPF já existente.
- Verificar se o produto e o cliente estão cadastrados antes de realizar uma venda.
- Impedir vendas de produtos sem estoque.
- Impedir quantidades de venda iguais ou inferiores a zero.
- Impedir vendas com quantidade superior ao estoque disponível.
- Verificar se existem registros antes de consultar produtos, clientes ou compras.
- Informar o usuário quando uma opção inválida é selecionada nos menus.

## 7. Como executar o projeto

Para executar o sistema, é necessário ter o Python 3 instalado no computador.

Siga as etapas:

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o terminal integrado.
3. Certifique-se de que os três arquivos estejam na mesma pasta:
   - `main.py`
   - `produtos.py`
   - `clientes.py`
4. Execute o seguinte comando no terminal:

```bash
python main.py
```

Após a execução, o menu principal será apresentado, permitindo acessar as funcionalidades disponíveis.

## 8. Armazenamento dos dados

O sistema utiliza listas e objetos para armazenar as informações durante a execução do programa.

Os produtos, clientes e históricos de compras permanecem disponíveis enquanto o programa estiver em funcionamento.

Como não foi implementado um banco de dados ou sistema de armazenamento em arquivos, os registros são perdidos quando o programa é encerrado.

## 9. Considerações finais

O desenvolvimento do projeto Loja de Eletrônicos permitiu colocar em prática os principais conceitos estudados durante as aulas de Python.

A construção do sistema possibilitou compreender melhor a utilização de funções, listas, estruturas condicionais, estruturas de repetição, modularização e programação orientada a objetos.

Além disso, o projeto demonstrou como diferentes módulos podem trabalhar em conjunto para formar um sistema organizado, com funcionalidades voltadas ao gerenciamento de produtos, clientes, estoque e vendas.

## 10. Integrantes do grupo

- Integrante 1: Luan Rodrigues (Trocou de faculdade)
- Integrante 2: Davi Miguel
- Integrante 3: Heitor