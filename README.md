# Sistema Financeiro - Python + FastAPI + PyQt6

## Descrição
   Este projeto integra backend e frontend usando Python, com uma interface gráfica desenvolvida em PyQt6 e backend construído com FastAPI.

   Funcionalidades:
      - Cadastro de receitas e despesas
      - Cálculo automático do saldo
      - Comunicação entre frontend e backend via requisições HTTP

## Tecnologias Utilizadas
   - Linguagem: Python
   - Backend: FastAPI, SQLAlchemy, SQLite, Pydantic
   - Frontend: PyQt6
   - Comunicação: Requests
   - Servidor: Uvicorn
   - Ambiente Virtual: venv

## Como Executar

1. Crie o ambiente virtual:   
   - python -m venv venv
   - venv\Scripts\activate

2. Instale as dependências:
   - pip freeze > requirements.txt
   - pip install -r requirements.txt

3. Inicialize o banco de dados:
   - python -c "from backend.database import Base, engine; Base.metadata.create_all(bind=engine)"

4. Rode o backend:
   - uvicorn backend.main:app --reload

5. Em outro terminal, ative novamente o ambiente virtual e rode o frontend:
   - cd frontend
   - python app.py

Interface
   - O sistema exibe uma interface gráfica amigável para controle financeiro pessoal.

Observação
   - Para sair do ambiente virtual:
      - deactivate
 
