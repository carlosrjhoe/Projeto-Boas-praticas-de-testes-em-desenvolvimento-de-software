# Projeto Boas praticas de testes em desenvolvimento de software

Código produzido como parte do artigo sobre Desenvolvimento Web com Django da Python, para aplicação dos conceitos básicos de testes com Pytest e Selenium
e saiba mais!

## Instalação

Primeiro, recomenda-se a criação de um ambiente virtual.

```bash
python -m venv venv
```

Segundo, ativar ambiente virtual.

```bash
.\venv\Scripts\activate
```

_Quer saber mais ambientes virtuais? Então [acesse o link para nosso post 
sobre ambientes virtuais no Python](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)!_

Com seu ambiente virtual configurado, instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

## Execução

Para executar o servidor de testes do Django, execute:

```bash
python manage.py runserver
```
