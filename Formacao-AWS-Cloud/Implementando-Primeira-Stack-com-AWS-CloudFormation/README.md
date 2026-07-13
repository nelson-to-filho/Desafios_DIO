# Implementando uma Stack com AWS CloudFormation

## Sobre o desafio

Este projeto foi desenvolvido como parte da Formação AWS Cloud da DIO. O objetivo do laboratório foi compreender como o AWS CloudFormation pode ser utilizado para criar e gerenciar recursos da AWS por meio de infraestrutura como código.

Durante a prática, foram estudados os conceitos de templates, stacks, parâmetros, recursos e automação da infraestrutura.

## O que é o AWS CloudFormation?

O AWS CloudFormation é um serviço que permite descrever recursos da AWS utilizando arquivos de configuração em YAML ou JSON.

Com ele, é possível criar, atualizar e excluir vários recursos de forma automatizada, reduzindo configurações manuais e facilitando a reprodução de ambientes.

## Exemplo de template

O exemplo abaixo representa um template simples para criação de um bucket no Amazon S3:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: Stack simples para criação de um bucket S3

Resources:
  BucketDoProjeto:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled

Outputs:
  NomeDoBucket:
    Description: Nome do bucket criado
    Value: !Ref BucketDoProjeto
```

## Etapas realizadas

1. Acesso ao serviço AWS CloudFormation pelo Console da AWS.
2. Criação de um template utilizando YAML.
3. Definição dos recursos que seriam criados.
4. Criação de uma nova stack.
5. Envio e validação do template.
6. Acompanhamento dos eventos de criação da stack.
7. Verificação dos recursos criados.
8. Exclusão da stack ao final do laboratório para evitar cobranças desnecessárias.

## Conceitos aprendidos

- Infraestrutura como código;
- Criação e gerenciamento de stacks;
- Estrutura de templates YAML;
- Definição de recursos e propriedades;
- Utilização de outputs;
- Acompanhamento dos eventos de uma stack;
- Atualização e exclusão automatizada de recursos;
- Padronização e reprodução de ambientes.

## Principais benefícios

O uso do AWS CloudFormation permite:

- Automatizar a criação da infraestrutura;
- Reduzir erros de configuração manual;
- Reutilizar templates em diferentes ambientes;
- Manter a infraestrutura documentada;
- Facilitar atualizações e exclusões de recursos;
- Criar ambientes de forma padronizada.

## Conclusão

Este laboratório permitiu compreender, na prática, como o AWS CloudFormation auxilia na automação e no gerenciamento da infraestrutura em nuvem.

A utilização de templates torna o processo mais organizado, reproduzível e seguro, além de facilitar a criação de ambientes semelhantes para desenvolvimento, testes e produção.

## Referência

- [Documentação oficial do AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/)

---

Desenvolvido por **Nelson Tavares de Oliveira Filho** como parte da Formação AWS Cloud da [DIO](https://www.dio.me/).
