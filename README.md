# Questionário

- **Quais linguagens de programação você conhece?** 
Python, Java e JavaScript.

- **Você já usou git?**
Já utilizei git, durante o curso do Geração Caldeira 2024, na Residência em Ciência de Dados no Instituto Eldorado e Cursos por fora como Alura e Rocketseat.

- **Como você explicaria para uma pessoa leiga o que é um banco de dados?**
Um Banco de Dados é como se fosse um conjunto de gavetas onde são lançados e armazenados informações pessoais, como senhas, CPF como também dados da empresa, são nessas gavetas que o sistema irá buscar exatamente os dados que você precisa.

- **O que é uma variável na programação?**
Na programação uma "Variável" é um espaço na memória do computador, para guardar um valor para ser usado depois, como exemplo uma caixa nomeada "idade" e "25" é seu conteúdo(valor), este valor é trocado ou consultado pelo sistema desenvolvido, uma variável pode ser, Int(números inteiros), Float(números decimais) e String(texto).

- **Analisando o seu código, escolha um princípio de programação que melhor te define.**
O que me define seria a Estrutura de Dados, pois através de uma organização na criação do código, auxilia no entendimento e na localização de arquivos ou dados. Entre outros princípios como SRP(Single Responsibility Principle) e DRY(Don't Repeat Yourself). 

- **Conte um problema que já resolveu com programação e qual foi o maior desafio envolvido.**
O problema que tive foi mais um desafio, onde eu precisava criar um site utilizando uma API, o problema foi em achar alguma API que não tivesse custo, após encontrar uma API para o projeto o desafio maior foi conseguir uma KEY da mesma, após um tempo de pesquisa consegui a KEY para dar sequência no projeto, o qual era um site que informava a temperatura em tempo real da cidade que fosse informada.

# ✈ Sistema de Reserva de Voos

Aplicação web para gerenciamento de reservas de voos desenvolvida com Django e PostgreSQL.

---

## 📋 Funcionalidades

- **Gerenciamento de aviões** — cadastro e controle de capacidade
- **Gerenciamento de voos** — criação de voos com origem, destino, data e horário
- **Gerenciamento de clientes** — cadastro com informações de contato
- **Gerenciamento de reservas** — reserva de assentos com validação automática
- **Autenticação** — níveis de acesso para admin e cliente
- **Reserva self-service** — clientes podem reservar seus próprios assentos após o login

---

## 🛠 Tecnologias utilizadas

- Python 3.13
- Django 6.0
- PostgreSQL

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Lucas05DEV/Teste-DEV---aDoc.git
cd teste-dev-adoc
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

Se apresentar algum erro na criação da .venv execute novamente: python -m venv .venv
Ou utilize: python -m venv .venv --without-pip

# Windows
.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco PostgreSQL e configure a conexão em `reserva_voos/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário (admin)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse a aplicação em `http://127.0.0.1:8000/register/`

---

## 👥 Perfis de usuário

| Perfil | Acesso |
|--------|--------|
| **Admin** (`is_staff=True`) | CRUD completo — aviões, voos, clientes, reservas |
| **Cliente** (`is_staff=False`) | Visualizar voos e fazer reservas self-service |

### Criando uma conta de cliente

Clientes podem se registrar em `/register/` ou ser criados via Django shell:

```python
from django.contrib.auth.models import User
User.objects.create_user(username='cliente1', password='senha123')
```

---

## 📁 Estrutura do projeto

```
teste-dev-adoc/
├── reserva_voos/          # Configurações do projeto
│   ├── settings.py
│   └── urls.py
├── voos/                  # App principal
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── airplanes/
│   │   ├── flights/
│   │   ├── clients/
│   │   └── reservations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🗄 Modelos de dados

### Airplane (Avião)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| identification | CharField | Identificação única |
| max_capacity | PositiveIntegerField | Capacidade máxima de passageiros |

### Flight (Voo)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| airplane | ForeignKey | Avião associado |
| origin | CharField | Cidade de origem |
| destination | CharField | Cidade de destino |
| date | DateField | Data do voo |
| time | TimeField | Horário de partida |

### Client (Cliente)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| user | OneToOneField | Usuário Django |
| name | CharField | Nome completo |
| email | EmailField | Email único |
| telephone | CharField | Telefone de contato |

### Reservation (Reserva)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| client | ForeignKey | Cliente associado |
| flight | ForeignKey | Voo associado |
| seat_number | PositiveIntegerField | Número do assento |
| status | CharField | ativa / cancelada |
| reservation_date | DateTimeField | Preenchido automaticamente |

---

## ✅ Regras de negócio

- O número do assento não pode exceder a capacidade do avião
- Um cliente não pode ter duas reservas ativas no mesmo voo
- O mesmo assento não pode ser reservado duas vezes no mesmo voo
- Origem e destino não podem ser iguais
