
# Automatizando Workflows com AWS Step Functions

## Sobre o desafio

Este projeto foi desenvolvido como parte da Formação AWS Cloud da DIO. O objetivo do desafio é consolidar os conhecimentos sobre automação de workflows utilizando o AWS Step Functions e documentar os principais conceitos aprendidos durante as aulas.

O AWS Step Functions permite organizar diferentes etapas de uma aplicação em um fluxo visual, facilitando a execução, o acompanhamento e o tratamento de possíveis falhas.

## O que é o AWS Step Functions?

O AWS Step Functions é um serviço de orquestração de workflows da AWS. Ele permite coordenar serviços e tarefas por meio de máquinas de estado, definindo a ordem em que cada etapa deve ser executada.

Com esse serviço, é possível criar fluxos que incluem:

- Execução de tarefas;
- Validação de informações;
- Tomada de decisões;
- Repetição automática em caso de falhas;
- Execução de tarefas em paralelo;
- Controle do início e do fim de cada processo.

## Principais conceitos estudados

### Máquina de estado

A máquina de estado representa todo o workflow. Ela define as etapas do processo, as regras de transição e o comportamento esperado em cada situação.

### Estados

Os estados representam as diferentes etapas do fluxo. Entre os principais estão:

- **Task:** executa uma tarefa ou serviço;
- **Choice:** cria uma condição e direciona o fluxo;
- **Wait:** aguarda um período antes de continuar;
- **Parallel:** executa diferentes tarefas ao mesmo tempo;
- **Succeed:** indica que o processo foi concluído com sucesso;
- **Fail:** indica que ocorreu uma falha;
- **Pass:** transmite informações para a próxima etapa sem executar uma tarefa.

### Tratamento de erros

O Step Functions permite configurar tentativas automáticas quando uma etapa apresenta erro. Também é possível direcionar a execução para um fluxo alternativo, evitando que todo o processo seja interrompido sem controle.

Os principais recursos utilizados para isso são:

- **Retry:** tenta executar novamente uma etapa;
- **Catch:** captura o erro e direciona o fluxo para outra etapa.

### Amazon States Language

Os workflows são definidos utilizando a Amazon States Language, uma linguagem baseada em JSON. Por meio dela, são configurados os estados, transições, condições e tratamentos de erro da máquina de estado.

## Exemplo de workflow

Um fluxo simples pode receber uma informação, validar os dados e executar uma ação de acordo com o resultado da validação.

```mermaid
flowchart LR
    A[Receber dados] --> B[Validar informações]
    B --> C{Dados válidos?}
    C -- Sim --> D[Executar processamento]
    C -- Não --> E[Registrar erro]
    D --> F[Finalizar workflow]
    E --> F
