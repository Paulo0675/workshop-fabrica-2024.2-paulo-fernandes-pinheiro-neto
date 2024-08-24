# workshop-fabrica-2024.2-paulo-fernandes
 Fábrica de Software 2024.2 - Workshop
Desenvolvido Por:
- Paulo Fernandes Pinheiro Neto

---

### README para a branch `main`

# Projeto de Organização Pessoal de Tarefas

Este projeto é uma aplicação web desenvolvida em Django, com o objetivo de organizar tarefas e suas respectivas categorias. Ele permite que os usuários criem, editem, excluam e concluam tarefas, bem como gerenciem categorias associadas.

## Funcionalidades

- **CRUD para Tarefas**: Criação, leitura, atualização e exclusão de tarefas.
- **CRUD para Categorias**: Criação, leitura, atualização e exclusão de categorias.
- **Conclusão de Tarefas**: Marcar tarefas como concluídas.
- **Interface Amigável**: Utiliza templates do Django para exibição dos dados.

## Funcionalidades Incluídas

- **Modelos de Dados**: Define as entidades `Todo` (Tarefa) e `Category` (Categoria).
- **CRUD para Tarefas e Categorias**: Implementa operações de criação, leitura, atualização e exclusão.
- **Template Base**: Um template HTML base para facilitar a criação de novas páginas.
- **Boas Práticas**: Estrutura do projeto seguindo boas práticas de organização de código.
- **Boas Práticas e Commits Semânticos**: O código é organizado seguindo boas práticas de programação, e os commits são feitos utilizando convenções semânticas.

## Estrutura do Projeto

- **models.py**: Define os modelos de dados para tarefas e categorias, contendo as definições das entidades `Todo` (Tarefa) e `Category` (Categoria).
- **views.py**: Implementa as views baseadas em classe (CBVs) para manipulação de tarefas e categorias.
- **urls.py**: Configuração das URLs da aplicação.
- **templates**: Diretório contendo os templates HTML para as páginas de tarefas e categorias.
- **static**: Diretório para arquivos estáticos como CSS, JavaScript e imagens.
- **forms.py**: Define os formulários utilizados na aplicação.
- **admin.py**: Configurações do Django Admin para gerenciar tarefas e categorias.

## Requisitos

- Python 3.8+
- Django 3.2+
- SQLite (ou outro banco de dados configurado no `settings.py`)

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Execute as migrações:
    ```bash
    python manage.py migrate
    ```
7. Crie um superusuário para acessar o Django Admin:
    ```bash
    python manage.py createsuperuser
    ```
8. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
9. Acesse a aplicação em `http://localhost:8000`.

---
