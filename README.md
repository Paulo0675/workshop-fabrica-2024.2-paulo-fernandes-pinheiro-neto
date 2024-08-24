# workshop-fabrica-2024.2-paulo-fernandes
 Fábrica de Software 2024.2 - Workshop
 Desenvolvido por: 
 - Paulo Fernandes Pinheiro Neto

---

### README para a branch `projeto-tarefas`

# Projeto de Tarefas com Integração de APIs

Considerando o arquivo tests.py este projeto é uma extensão do modelo básico de organização de tarefas, com a adição de integração com APIs externas para manipulação de dados.

## Funcionalidades Adicionais

- **Testes de Integração com API**: Implementa chamadas para uma API externa para a criação, atualização e exclusão de tarefas.
- **Testes de CRUD Estendido**: Além das funcionalidades básicas, as operações CRUD interagem com a API externa para manter a consistência dos dados.
- **Boas Práticas e Commits Semânticos**: O código é organizado seguindo boas práticas de programação, e os commits são feitos utilizando convenções semânticas.

## Estrutura

- **views.py**: Além das CBVs básicas, inclui métodos para integração com a API externa.
- **models.py**: Definição dos modelos de dados permanece a mesma.
- **tests.py**: Contém testes para validar a integração com a API.
- **templates**: Inclui templates para as views, adaptados para refletir as operações realizadas via API.

## Como Executar

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure as variáveis de ambiente para a API externa.
4. Execute as migrações e inicie o servidor de desenvolvimento.
5. Acesse a aplicação em `http://localhost:8000`.

--- 
