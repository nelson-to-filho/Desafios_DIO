
# Gerenciamento de Instâncias EC2 na AWS

## Sobre o desafio

Este projeto foi desenvolvido como parte da formação em AWS da DIO. O objetivo é registrar os principais conhecimentos adquiridos sobre a criação, configuração e gerenciamento de instâncias Amazon EC2.

O Amazon EC2 permite criar servidores virtuais na nuvem de acordo com as necessidades de cada aplicação, oferecendo diferentes opções de processamento, memória, armazenamento, sistema operacional e modelo de pagamento.

## O que é o Amazon EC2?

O Amazon Elastic Compute Cloud, conhecido como Amazon EC2, é um serviço da AWS utilizado para provisionar máquinas virtuais na nuvem.

Essas máquinas virtuais são chamadas de instâncias e podem ser utilizadas para hospedar sites, executar aplicações, criar ambientes de desenvolvimento, processar dados e realizar diversas outras tarefas.

## Principais conceitos estudados

### AMI

A Amazon Machine Image é o modelo utilizado para criar uma instância EC2. Ela contém o sistema operacional e pode incluir programas e configurações previamente instalados.

Alguns exemplos são:

- Amazon Linux;
- Ubuntu;
- Windows Server;
- Red Hat Enterprise Linux.

### Tipo de instância

O tipo de instância define a quantidade de recursos computacionais disponíveis, como processador, memória e capacidade de rede.

A escolha deve ser feita de acordo com a necessidade da aplicação, buscando equilíbrio entre desempenho e custo.

### Par de chaves

O par de chaves permite realizar o acesso seguro à instância.

Em servidores Linux, normalmente o acesso é feito por SSH. Em servidores Windows, a chave pode ser utilizada para obter a senha de acesso remoto.

O arquivo da chave privada deve ser armazenado com segurança, pois a AWS não permite baixá-lo novamente após sua criação.

### Security Groups

Os Security Groups funcionam como um firewall virtual para as instâncias EC2.

Eles controlam quais conexões de entrada e saída são permitidas. É possível liberar portas específicas, como:

- Porta 22 para SSH;
- Porta 80 para HTTP;
- Porta 443 para HTTPS;
- Porta 3389 para acesso remoto ao Windows.

Uma boa prática é permitir somente as portas realmente necessárias e restringir o acesso por endereço IP sempre que possível.

### Armazenamento EBS

O Amazon Elastic Block Store fornece volumes de armazenamento que podem ser conectados às instâncias EC2.

Esses volumes armazenam o sistema operacional, aplicações e arquivos da instância. Dependendo da configuração, os dados podem continuar disponíveis mesmo após a instância ser interrompida.

## Ciclo de vida de uma instância

Uma instância EC2 pode passar por diferentes estados:

- **Pending:** a instância está sendo iniciada;
- **Running:** a instância está em execução;
- **Stopping:** a instância está sendo interrompida;
- **Stopped:** a instância está desligada;
- **Terminated:** a instância foi encerrada definitivamente.

Interromper uma instância não é o mesmo que encerrá-la. Quando uma instância é encerrada, ela não pode ser iniciada novamente.

## Modelos de contratação

A AWS oferece diferentes formas de contratação para as instâncias EC2:

### Instâncias sob demanda

O pagamento é realizado de acordo com o tempo de utilização, sem necessidade de compromisso de longo prazo.

É uma opção adequada para testes, aplicações temporárias e cargas de trabalho que podem variar.

### Instâncias reservadas

São indicadas para aplicações que serão utilizadas por períodos mais longos. Elas podem oferecer preços menores em troca de um compromisso de utilização.

### Instâncias Spot

Utilizam a capacidade ociosa da AWS e podem apresentar valores reduzidos.

Porém, podem ser interrompidas pela AWS quando essa capacidade for necessária, sendo mais indicadas para tarefas que toleram interrupções.

## Responsabilidade do cliente

A AWS é responsável pela segurança da infraestrutura física, incluindo servidores, rede, energia e datacenters.

O cliente é responsável por configurar e gerenciar:

- Sistema operacional;
- Aplicações instaladas;
- Controle de usuários;
- Atualizações de segurança;
- Security Groups;
- Dados armazenados na instância.

Esse conceito faz parte do modelo de responsabilidade compartilhada da AWS.

## Boas práticas

Durante o gerenciamento de uma instância EC2, algumas práticas importantes são:

- Escolher um tipo de instância adequado para a aplicação;
- Liberar somente as portas necessárias;
- Evitar utilizar a conta root nas atividades diárias;
- Utilizar usuários e permissões do IAM;
- Proteger o arquivo da chave privada;
- Manter o sistema operacional atualizado;
- Monitorar os recursos utilizados;
- Interromper ou encerrar instâncias que não estão sendo usadas;
- Verificar os custos regularmente;
- Criar backups dos dados importantes.

## Principais aprendizados

Com este laboratório, foi possível compreender que o gerenciamento de uma instância EC2 envolve mais do que apenas criar uma máquina virtual.

É necessário analisar o tipo de instância, sistema operacional, armazenamento, segurança, forma de acesso e modelo de cobrança.

Também ficou evidente que pequenas configurações, como deixar portas abertas desnecessariamente ou manter recursos sem utilização, podem gerar riscos de segurança e custos adicionais.

## Conclusão

O Amazon EC2 é um serviço flexível e importante dentro da AWS. Ele permite criar ambientes computacionais de maneira rápida, sem a necessidade de comprar e manter servidores físicos.

O uso correto do serviço exige atenção às configurações de segurança, desempenho e custos. Os conhecimentos adquiridos neste desafio servirão como base para futuras implementações e projetos utilizando computação em nuvem.

## Documentação

- [Documentação oficial do Amazon EC2](https://docs.aws.amazon.com/ec2/)
- [Guia do usuário do Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Modelo de responsabilidade compartilhada da AWS](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Autor

Desenvolvido por [Nelson Filho](https://github.com/nelson-to-filho) durante a formação em AWS da DIO.
