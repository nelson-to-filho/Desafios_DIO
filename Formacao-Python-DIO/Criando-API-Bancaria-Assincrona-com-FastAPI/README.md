# API Bancária Assíncrona com FastAPI

Projeto desenvolvido durante a Formação Python Fundamentals da DIO, com o objetivo de construir e testar uma API bancária assíncrona utilizando FastAPI.

A aplicação permite criar contas, registrar depósitos e saques, consultar transações e proteger as operações utilizando autenticação JWT.

## Funcionalidades

- Autenticação com JWT;
- Criação de contas bancárias;
- Listagem de contas;
- Registro de depósitos;
- Registro de saques;
- Consulta do extrato de uma conta;
- Validação de valores maiores que zero;
- Bloqueio de saques superiores ao saldo disponível;
- Documentação interativa com Swagger;
- Endpoint para verificar o status da API.

## Tecnologias utilizadas

- Python 3.11;
- FastAPI;
- Uvicorn;
- SQLite;
- SQLAlchemy;
- Databases;
- Alembic;
- Pydantic;
- PyJWT;
- Poetry.

## Estrutura do projeto

```text
Criando-API-Bancaria-Assincrona-com-FastAPI/
├── migrations/
├── src/
├── .env.example
├── .gitignore
├── alembic.ini
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Configuração do ambiente

O projeto utiliza Python 3.11 e Poetry para gerenciamento das dependências.

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/nelson-to-filho/Desafios_DIO.git
cd Desafios_DIO/Formacao-Python-DIO/Criando-API-Bancaria-Assincrona-com-FastAPI
```

Instale as dependências:

```bash
poetry install --no-root
```

Crie o arquivo `.env` utilizando o modelo disponível:

```bash
cp .env.example .env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

## Banco de dados

O ambiente local utiliza SQLite:

```env
ENVIRONMENT="local"
DATABASE_URL="sqlite:///./bank.db"
```

Execute as migrações para criar as tabelas:

```bash
poetry run alembic upgrade head
```

## Executando a API

Inicie o servidor com:

```bash
poetry run uvicorn src.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa poderá ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Principais endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/auth/login` | Gera o token JWT |
| `GET` | `/accounts/` | Lista as contas |
| `POST` | `/accounts/` | Cria uma conta |
| `GET` | `/accounts/{id}/transactions` | Consulta o extrato |
| `POST` | `/transactions/` | Registra depósito ou saque |
| `GET` | `/` | Verifica o status da API |

## Exemplos de uso

### Autenticação

```json
{
  "user_id": 1
}
```

### Criação de conta

```json
{
  "user_id": 1,
  "balance": 1000
}
```

### Depósito

```json
{
  "account_id": 1,
  "type": "deposit",
  "amount": 500
}
```

### Saque

```json
{
  "account_id": 1,
  "type": "withdrawal",
  "amount": 200
}
```

## Validações testadas

Durante os testes, foram verificados os seguintes cenários:

- criação de conta com sucesso;
- depósito em conta existente;
- saque com saldo disponível;
- consulta do histórico de transações;
- bloqueio de saque por saldo insuficiente;
- rejeição de depósitos e saques com valores negativos;
- acesso aos endpoints protegidos com autenticação JWT.

## Melhoria implementada

Foi criada uma rota inicial para verificar rapidamente se a API está funcionando:

```http
GET /
```

Resposta:

```json
{
  "status": "online",
  "message": "API Bancária Assíncrona funcionando",
  "documentation": "/docs"
}
```

## Aprendizados

O projeto permitiu aplicar conceitos de APIs REST, programação assíncrona, autenticação JWT, validação de dados, persistência com SQLite, migrações de banco de dados e documentação automática com OpenAPI.

## Referência

Projeto baseado no desafio disponibilizado pela Digital Innovation One:

- [Trilha Python DIO](https://github.com/digitalinnovationone/trilha-python-dio)

---

Desenvolvido por **Nelson Tavares de Oliveira Filho** durante a Formação Python Fundamentals da DIO.