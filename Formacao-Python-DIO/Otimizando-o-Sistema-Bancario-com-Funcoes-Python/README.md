# Sistema Bancário com Funções Python

Projeto desenvolvido como parte da **Formação Python Fundamentals**, da plataforma [DIO](https://www.dio.me/).

O objetivo do desafio é aprimorar um sistema bancário simples, organizando suas operações em funções e aplicando conceitos fundamentais da linguagem Python.

## Sobre o projeto

O sistema funciona por meio de um menu no terminal e permite realizar operações bancárias, cadastrar usuários e criar contas.

O código foi desenvolvido com base no projeto apresentado pela DIO e recebeu pequenas melhorias de organização, validação e experiência do usuário.

## Funcionalidades

- Realizar depósitos;
- Realizar saques;
- Exibir extrato bancário;
- Cadastrar novos usuários;
- Criar contas bancárias;
- Listar contas cadastradas;
- Validar saldo disponível;
- Validar limite por saque;
- Controlar a quantidade diária de saques;
- Impedir o cadastro duplicado de CPF.

## Regras do sistema

- O valor do depósito deve ser positivo;
- O limite máximo por saque é de R$ 500,00;
- São permitidos até três saques;
- O saque não pode ser maior que o saldo disponível;
- O usuário precisa estar cadastrado antes da criação de uma conta;
- Cada CPF pode possuir apenas um cadastro de usuário;
- Todas as contas utilizam a agência `0001`.

## Melhorias implementadas

Além das funcionalidades apresentadas no código-base, foram adicionadas algumas melhorias:

- Tratamento de opções digitadas em letras maiúsculas ou minúsculas;
- Remoção automática da pontuação do CPF;
- Validação da quantidade de números do CPF;
- Mensagens mais claras para operações inválidas;
- Mensagem específica quando nenhuma conta foi cadastrada;
- Organização da execução por meio da função `main`;
- Uso de parâmetros posicionais e nomeados nas funções;
- Correção e atualização do controle de quantidade de saques.

## Conceitos utilizados

- Funções;
- Parâmetros posicionais;
- Parâmetros nomeados;
- Estruturas condicionais;
- Estruturas de repetição;
- Listas;
- Dicionários;
- Manipulação de strings;
- Formatação de valores monetários;
- Modularização e organização de código.

## Estrutura do projeto

```text
Otimizando-o-Sistema-Bancario-com-Funcoes-Python/
├── desafio.py
└── README.md
```

## Como executar

É necessário possuir o Python instalado no computador.

Abra o terminal dentro da pasta do projeto e execute:

```bash
python desafio.py
```

No Windows, também pode ser utilizado:

```bash
py desafio.py
```

## Menu do sistema

```text
================ MENU ================

[d]  Depositar
[s]  Sacar
[e]  Exibir extrato
[nu] Cadastrar usuário
[nc] Criar conta
[lc] Listar contas
[q]  Sair
```

## Referência

Projeto baseado no desafio disponibilizado no repositório oficial da DIO:

[Trilha Python DIO — Sistema Bancário](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/01%20-%20Estrutura%20de%20dados/desafio.py)

## Autor

Desenvolvido por **Nelson Tavares de Oliveira Filho** como parte dos desafios de formação da DIO.