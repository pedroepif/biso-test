# API de Recomendação de Filmes

## Descrição

Este projeto é uma API de recomendação de filmes, utilizando FastAPI e Scikit-learn. A API fornece recomendações personalizadas de filmes com base no histórico de visualizações dos usuários, suas avaliações e preferências, como gêneros, diretores e atores favoritos.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** FastAPI
- **Banco de Dados:** SQLite
- **Bibliotecas:** SQLAlchemy, Scikit-learn

## Funcionalidades

- **Listar Filmes:** Retorna todos os filmes disponíveis na plataforma.
- **Recomendações Personalizadas:** Gera uma lista de filmes recomendados para um usuário com base em suas preferências e histórico.

## Instalação

Para utilizar instalar e iniciar o projeto você pode fazer usando docker, a partir do comando:

```bash
docker compose up
```

Ou utilizando Python diretamente. Neste caso incialmente é necessário instalar as dependências presentes no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

Depois de instalado é necessário popular o banco de dado através do script:

```bash
python scripts/populate.py
```

Por fim, basta iniciar a FastAPI através do comando:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

Por fim, a API estará disponível na porta 8000 do seu ambiente.
