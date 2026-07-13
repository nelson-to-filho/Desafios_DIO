# Executando Tarefas Automatizadas com AWS Lambda e Amazon S3

## Sobre o projeto

Este projeto foi desenvolvido durante a Formação AWS Cloud da DIO. O objetivo do laboratório foi compreender como automatizar tarefas utilizando o AWS Lambda integrado ao Amazon S3.

A prática demonstra como uma função serverless pode ser executada automaticamente quando um arquivo é enviado para um bucket S3.

## Serviços utilizados

- **AWS Lambda:** executa o código sem a necessidade de administrar servidores;
- **Amazon S3:** armazena arquivos e gera eventos;
- **AWS IAM:** controla as permissões utilizadas pela função Lambda;
- **Amazon CloudWatch:** registra logs e informações sobre a execução da função.

## Funcionamento da automação

O fluxo estudado funciona da seguinte maneira:

1. Um arquivo é enviado para um bucket do Amazon S3;
2. O S3 identifica a criação do objeto;
3. Um evento é enviado para a função Lambda;
4. A função executa automaticamente a tarefa configurada;
5. Os resultados da execução podem ser acompanhados pelo CloudWatch Logs.

```text
Upload do arquivo
       ↓
   Amazon S3
       ↓
Evento ObjectCreated
       ↓
   AWS Lambda
       ↓
Amazon CloudWatch Logs
```

## Exemplo de função Lambda

O código abaixo representa uma função Lambda em Python que identifica o nome do bucket e do arquivo enviado:

```python
import json
import urllib.parse


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]

    object_key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    print(f"Arquivo recebido: {object_key}")
    print(f"Bucket de origem: {bucket_name}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Arquivo processado com sucesso.",
            "bucket": bucket_name,
            "file": object_key
        })
    }
```

## Etapas do laboratório

1. Criar um bucket no Amazon S3;
2. Criar uma função no AWS Lambda;
3. Definir o ambiente de execução da função;
4. Configurar uma função do IAM com as permissões necessárias;
5. Adicionar o Amazon S3 como gatilho da função;
6. Selecionar o evento de criação de objetos;
7. Publicar o código da função Lambda;
8. Enviar um arquivo para o bucket;
9. Verificar a execução da função;
10. Consultar os registros no CloudWatch Logs.

## Permissões

A função Lambda precisa de uma função de execução do IAM que permita:

- Registrar informações no CloudWatch Logs;
- Ler objetos do bucket S3, quando necessário;
- Acessar somente os recursos utilizados pela automação.

É importante aplicar o princípio do menor privilégio, concedendo apenas as permissões necessárias para a execução da tarefa.

## Principais aprendizados

Durante o laboratório, foram estudados os seguintes conceitos:

- Computação serverless;
- Funções orientadas a eventos;
- Integração entre AWS Lambda e Amazon S3;
- Configuração de gatilhos;
- Controle de acesso com o AWS IAM;
- Monitoramento com o Amazon CloudWatch;
- Automação de tarefas na nuvem.

## Benefícios da solução

A integração entre AWS Lambda e Amazon S3 permite:

- Executar tarefas automaticamente;
- Reduzir processos manuais;
- Processar arquivos assim que forem enviados;
- Escalar a execução de acordo com a demanda;
- Pagar apenas pelos recursos utilizados;
- Criar soluções sem gerenciar servidores.

## Possíveis aplicações

Essa arquitetura pode ser utilizada para:

- Processamento de imagens;
- Validação de arquivos;
- Conversão de formatos;
- Organização automática de documentos;
- Extração de informações;
- Geração de miniaturas;
- Envio de notificações;
- Processamento de logs.

## Boas práticas

- Utilizar permissões mínimas no IAM;
- Validar os dados recebidos pela função;
- Configurar logs para acompanhar as execuções;
- Evitar armazenar informações sensíveis diretamente no código;
- Tratar erros durante o processamento;
- Excluir recursos de laboratório que não serão mais utilizados.

## Conclusão

O laboratório demonstrou como o AWS Lambda pode ser integrado ao Amazon S3 para criar tarefas automatizadas e orientadas a eventos.

Essa arquitetura permite processar arquivos de forma escalável, reduzindo configurações manuais e eliminando a necessidade de administrar servidores.

## Referências

- [Documentação do AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [Documentação do Amazon S3](https://docs.aws.amazon.com/s3/)
- [AWS Lambda com Amazon S3](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)

---

Desenvolvido por **Nelson Tavares de Oliveira Filho** durante a Formação AWS Cloud da [DIO](https://www.dio.me/).
