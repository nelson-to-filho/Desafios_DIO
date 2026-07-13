# Desafio: Arquitetura de Microsserviços com Spring Boot e RabbitMQ

## 📝 Descrição do Projeto
Este projeto demonstra a construção de uma arquitetura baseada em microsserviços utilizando Java e Spring Boot. O objetivo principal é simular um ecossistema de e-commerce, implementando a comunicação entre serviços de forma eficiente e escalável.

A arquitetura é composta por dois microsserviços principais que interagem entre si utilizando tanto comunicação síncrona quanto assíncrona.

## 🏗️ Estrutura da Arquitetura

1. **Warehouse (Armazém):** 
   - Responsável por gerenciar o estoque e a logística dos produtos.
   - Fornece endpoints para consulta de disponibilidade.

2. **Storefront (Vitrine):**
   - Atua como a interface do cliente (backend for frontend).
   - Recebe os pedidos e interage com o Warehouse para validar e processar as solicitações.

## 🔄 Padrões de Comunicação

* **Síncrona (HTTP/REST):** Utilizada para consultas imediatas, como verificar se um produto específico está disponível no Warehouse no momento da compra.
* **Assíncrona (Mensageria com RabbitMQ):** Utilizada para o processamento de pedidos. O Storefront publica uma mensagem na fila informando que uma compra foi realizada, e o Warehouse consome essa mensagem no seu próprio tempo para dar baixa no estoque, garantindo que o sistema não trave caso haja alta demanda.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Java
* **Framework:** Spring Boot
* **Mensageria:** RabbitMQ
* **Arquitetura:** Microsserviços / REST API

## 🚀 Como Executar (Opcional - Caso decida subir o código)
1. Clone este repositório.
2. Certifique-se de ter o RabbitMQ rodando (via Docker ou local).
3. Inicie primeiro o microsserviço `warehouse`.
4. Em seguida, inicie o microsserviço `storefront`.
