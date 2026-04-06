# Sistema de Reserva de Voos - Desafio aDoc

[![Django](https://img.shields.io/badge/Django-6.0.3-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Sistema de gerenciamento de reservas de voos desenvolvido para o desafio técnico da empresa **aDoc**. Foi implementada operações CRUD para aviões, voos, clientes e reservas utilizando Django e PostgreSQL.

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação web completa que permita gerenciar reservas de voos, atendendo aos seguintes requisitos principais:

- ✅ Listar voos disponíveis com detalhes completos
- ✅ Cadastrar aviões com identificação única e capacidade
- ✅ Gerenciar voos (origem, destino, data e horário)
- ✅ Registrar clientes e associá-los a voos
- ✅ Sistema de reservas com assentos únicos

## 🏆 Bônus Implementados

- 🎨 **Interface Gráfica**: Templates responsivos com Bootstrap
- 🔐 **Autenticação**: Sistema completo de login obrigatório
- 🎫 **Localizador Único**: Geração automática de códigos de reserva
- 📊 **Dashboard**: Visualização detalhada de voos e assentos ocupados

## 📋 Requisitos Funcionais

### ✈️ Cadastro de Aviões

- Identificação única para cada avião
- Definição da capacidade máxima de passageiros
- Validação de unicidade do identificador

### 🛫 Gerenciamento de Voos

- Associação de voos a aviões existentes
- Especificação de origem, destino, data e horário
- Listagem completa de voos disponíveis

### 👥 Cadastro de Clientes

- Registro de nome e informações de contato
- Associação a reservas específicas

### 🎫 Reservas de Assentos

- Atribuição de assentos únicos por voo
- Validação de disponibilidade de assentos
- Geração automática de localizador de reserva

## 🏗️ Arquitetura Técnica

### Tecnologias Utilizadas

- **Backend**: Django 6.0.3 (Framework web Python)
- **Banco de Dados**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap
- **Autenticação**: Sistema nativo do Django
- **Validação**: Django Forms com regras customizadas

### Estrutura MTV (Model-Template-View)

- **Models**: Definem entidades (Airplane, Customer, Flight, Reservation)
- **Views**: Implementam lógica de negócio e operações CRUD
- **Templates**: Interface responsiva e intuitiva
- **Forms**: Validação robusta de dados

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- PostgreSQL
- Git

### Passos de Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/gustavo-cigaran/flight-reservation-system
    cd flight_reservation_project
    ```

2. **Configure o ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados:**

    ```bash
    cd flight_reservation
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Crie um superusuário:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Execute o servidor:**

    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação:**
    - URL: `http://127.0.0.1:8000/`
    - Faça login com suas credenciais

## 📊 Modelo de Dados

### Airplane (Avião)

- `identifier` (string, único): Identificação do avião
- `capacity` (inteiro): Capacidade máxima

### Customer (Cliente)

- `name` (string): Nome completo
- `email` (string): Email de contato

### Flight (Voo)

- `airplane` (FK): Avião associado
- `origin` (string): Cidade de origem
- `destination` (string): Cidade de destino
- `departure_time` (datetime): Data e horário

### Reservation (Reserva)

- `record_locator` (string, único): Código de 6 caracteres
- `customer` (FK): Cliente
- `flight` (FK): Voo
- `seat_number` (inteiro): Número do assento

## 🎮 Funcionalidades Implementadas

### Sistema de Autenticação

- Login obrigatório para todas as operações
- Proteção CSRF em formulários
- Sessões seguras

### Operações CRUD Completas

- **Aviões**: Criar, listar, editar, excluir
- **Voos**: Criar, listar, editar, excluir
- **Clientes**: Criar, listar, editar, excluir
- **Reservas**: Criar, editar, excluir

### Validações de Negócio

- Unicidade de identificadores de avião
- Assentos únicos por voo
- Capacidade máxima respeitada
- Localizadores únicos gerados automaticamente

### Interface Responsiva

- Templates modernos e intuitivos
- Navegação clara entre módulos
- Visualização de assentos ocupados
- Formulários validados

## 📁 Estrutura do Projeto

```
flight_reservation_project/
├── README.md                    # Esta documentação
├── requirements.txt            # Dependências Python
├── LICENSE                     # Licença MIT
├── flight_reservation/
│   ├── core/                   # App principal
│   │   ├── models.py          # Modelos de dados
│   │   ├── views.py           # Lógica de negócio
│   │   ├── forms.py           # Formulários
│   │   ├── admin.py           # Admin Django
│   │   ├── apps.py            # Configuração da app
│   │   ├── tests.py           # Testes unitários
│   │   ├── migrations/        # Migrações DB
│   │   └── templates/         # Templates HTML
│   │       ├── base.html      # Template base
│   │       ├── *_list.html    # Listagens
│   │       ├── *_registration.html  # Formulários
│   │       └── registration/  # Templates de auth
│   ├── flight_reservation/    # Configurações
│   │   ├── settings.py       # Configurações Django
│   │   ├── urls.py           # URLs principais
│   │   ├── wsgi.py           # WSGI
│   │   └── asgi.py           # ASGI
│   ├── db.sqlite3            # Banco SQLite
│   └── manage.py             # Gerenciador Django
```

## 🔗 URLs do Sistema

- `/admin/`: Interface administrativa
- `/airplanes/`: Gerenciamento de aviões
- `/flights/`: Listagem de voos
- `/customers/`: Gerenciamento de clientes
- `/flights/<id>/`: Detalhes do voo e reservas

## 🧪 Testes

O projeto inclui uma suíte completa de testes unitários cobrindo:

- ✅ Criação e validação de aviões
- ✅ Unicidade de identificadores de avião
- ✅ Gerenciamento de clientes
- ✅ Criação e validação de voos
- ✅ Sistema de reservas com localizadores únicos
- ✅ Validação de assentos únicos por voo

Para executar os testes:

```bash
cd flight_reservation
python manage.py test
```

**Resultado atual**: ✅ 7 testes passando

## 📝 Questionário Técnico

### Quais linguagens de programação você conhece?

- Python (Básico - Django)
- Java (Intermediário - Spring Framework)
- JavaScript (Intermediário - Node.js, React, Vue)
- Dart (Básico - Flutter)
- SQL (banco de dados)
- HTML/CSS (frontend básico)

### Você já usou git?

Sim, já utilizei Git para alguns projetos, incluindo:

- Commits semânticos
- Branches para features
- Resolução de conflitos
- GitHub para colaboração

### Como você explicaria para uma pessoa leiga o que é um banco de dados?

Diria que um banco de dados é como se fosse uma biblioteca contendo vários livros, onde cada livro contém registros que armazenam informações e essas informações ficam guardadas e organizadas.

### O que é uma variável na programação?

Uma variável é como uma caixinha onde guardamos um valor que pode mudar durante a execução do programa. É uma forma de armazenar dados temporariamente na memória do computador, fazendo com que o programa "lembre" e manipule informações. Por exemplo, uma variável pode guardar um nome de usuário ou o resultado de um cálculo matemático.

### Analisando o seu código, escolha um princípio de programação que melhor te define.

Na faculdade e curso técnico estudei os princípios **SOLID** e um princípio que procurei seguir nesse projeto foi o **Single Responsibility Principle (SRP)**. Cada classe e função tem uma responsabilidade única e bem definida, tornando o código mais modular, testável e fácil de manter. No projeto, cada model, view e form tem seu propósito claro e não se mistura com outras responsabilidades.

### Conte um problema que já resolveu com programação e qual foi o maior desafio envolvido.

Desenvolvi um sistema financeiro utilizando React no front-end e Java com Spring no back-end, antes utilizava o Notion mas ele é limitado tanto para filtrar algumas informações e realizar customizações visuais. Com isso resolvi desenvolver algo que me ajudasse a organizar minhas dívidas e ter um controle dos gastos mensais. O maior desafio foi a parte técnica, pois recém estava aprendendo a desenvolver APIs e integrar front e back-end. Tive dificuldades em lidar com requisições, estruturação de dados e tratamento de erros, o que exigiu bastante resiliência e atenção aos detalhes.

## 🧩 Desafio de Lógica

### Desafio 1: Two Sum

Encontrar índices de dois números que somam um target específico.

[Veja o desafio aqui!](desafio_two_sum/desafio.py)

**Desenvolvido para o desafio técnico da aDoc** 🚀
