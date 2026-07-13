# Automatizando Infraestrutura com AWS CloudFormation

## Sobre o projeto

Este projeto foi desenvolvido durante a Formação AWS Cloud da DIO, com o objetivo de compreender como automatizar a criação e o gerenciamento de recursos na AWS utilizando o AWS CloudFormation.

A proposta do laboratório foi aplicar o conceito de infraestrutura como código, substituindo configurações manuais por templates reutilizáveis e versionáveis.

## O que é o AWS CloudFormation?

O AWS CloudFormation é um serviço que permite criar, atualizar e excluir recursos da AWS de forma automatizada.

A infraestrutura é descrita em arquivos YAML ou JSON, chamados de templates. Esses arquivos podem definir recursos, configurações, parâmetros e informações de saída da stack.

## Conceitos utilizados

Durante o laboratório, foram trabalhados os seguintes conceitos:

- Infraestrutura como código;
- Templates em YAML;
- Criação e gerenciamento de stacks;
- Definição de recursos e propriedades;
- Uso de parâmetros;
- Configuração de outputs;
- Atualização automatizada da infraestrutura;
- Exclusão de recursos por meio da stack.

## Exemplo de template

O exemplo abaixo cria um bucket no Amazon S3 com versionamento habilitado:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description: Infraestrutura automatizada com AWS CloudFormation

Parameters:
  NomeDoProjeto:
    Type: String
    Default: projeto-cloudformation
    Description: Nome utilizado para identificar o projeto

Resources:
  BucketDoProjeto:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled
      Tags:
        - Key: Projeto
          Value: !Ref NomeDoProjeto
        - Key: Ambiente
          Value: Desenvolvimento

Outputs:
  NomeDoBucket:
    Description: Nome do bucket criado pela stack
    Value: !Ref BucketDoProjeto

  ArnDoBucket:
    Description: ARN do bucket criado
    Value: !GetAtt BucketDoProjeto.Arn
```

## Estrutura do template

O template utiliza as seguintes seções:

- `AWSTemplateFormatVersion`: informa a versão do formato do template;
- `Description`: apresenta uma descrição da infraestrutura;
- `Parameters`: permite receber valores durante a criação da stack;
- `Resources`: define os recursos que serão criados;
- `Outputs`: apresenta informações importantes após a criação dos recursos.

## Etapas da automação

O processo de automação com o AWS CloudFormation pode ser realizado da seguinte forma:

1. Criar o template da infraestrutura;
2. Validar a estrutura do arquivo YAML;
3. Acessar o AWS CloudFormation;
4. Criar uma nova stack;
5. Enviar o template;
6. Informar os parâmetros necessários;
7. Revisar as configurações;
8. Iniciar a criação da stack;
9. Acompanhar os eventos de implantação;
10. Verificar os recursos criados.

Quando a infraestrutura não for mais necessária, a stack pode ser excluída. Dessa forma, os recursos gerenciados pelo template também são removidos de maneira automatizada.

## Benefícios da automação

A utilização do AWS CloudFormation oferece benefícios como:

- Redução de erros causados por configurações manuais;
- Padronização dos ambientes;
- Reutilização de templates;
- Facilidade para atualizar recursos;
- Controle de versão da infraestrutura;
- Implantação mais rápida;
- Melhor organização e documentação dos recursos.

## Boas práticas

Algumas boas práticas importantes são:

- Validar o template antes da implantação;
- Utilizar nomes claros para recursos e parâmetros;
- Organizar os recursos com tags;
- Evitar informações sensíveis diretamente no template;
- Acompanhar os eventos da stack;
- Excluir recursos de laboratório para evitar cobranças;
- Manter os templates versionados no GitHub.

## Aprendizados

Este laboratório demonstrou que o AWS CloudFormation facilita a criação de infraestruturas reproduzíveis e padronizadas.

Também foi possível compreender que a infraestrutura como código melhora o controle das configurações, facilita atualizações e permite que diferentes ambientes sejam criados seguindo a mesma estrutura.

## Conclusão

A automação com AWS CloudFormation torna o gerenciamento da infraestrutura mais eficiente, seguro e organizado.

Com o uso de templates, os recursos deixam de depender exclusivamente de configurações manuais e passam a ser definidos de maneira clara, reutilizável e versionável.

## Referências

- [Documentação oficial do AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/)
- [Referência de templates do AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/)

---

Desenvolvido por **Nelson Tavares de Oliveira Filho** durante a Formação AWS Cloud da [DIO](https://www.dio.me/).
