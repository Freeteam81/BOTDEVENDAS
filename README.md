# BOTDEVENDAS

Este projeto implementa um bot de vendas simples utilizando Flask e a API do ChatGPT.

## Requisitos

- Python 3.8+
- Conta na OpenAI (chave `OPENAI_API_KEY`)

## Instalacao

```bash
pip install -r requirements.txt
```

## Execucao

Defina a variavel `OPENAI_API_KEY` com sua chave e execute:

```bash
python app.py
```

Envie mensagens para o endpoint `/chat` usando `POST` com JSON:

```json
{"message": "Quero saber mais sobre o plano premium"}
```

A resposta trara a mensagem do ChatGPT e links de compra quando apropriado.

