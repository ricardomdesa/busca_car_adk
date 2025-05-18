# BuscaCar

BuscaCar é um AI-powered agent que usa o [google-adk](https://pypi.org/project/google-adk/) library to search and suggest used car ads.

Link colab, um jeito mais rapido de rodar: 
https://colab.research.google.com/drive/1xQ49DvbNyKwO8CUwNpFv6wufYo4GHYRV?usp=sharing

## Features

- Busque por veiculos e deixe a IA te trazer as informacoes importantes
- Sugestões de anúncios de carros usados
- Integração com o Google Search para busca de anúncios

## Requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências
- criar um arquivo .env com as variaveis de ambiente do google adk GOOGLE_ADK_API_KEY e GOOGLE_API_KEY=<sua chave>

## Instalação

Git Clone o repository do github e instale as dependencias:

```bash
git clone https://github.com/ricardomdesa/busca_car_adk.git
cd busca_car_adk
poetry install

poetry shell
```

## Usage

```bash
# no terminal rodar:
python src/main.py
```