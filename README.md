# 🏠 Property Market Analyzer

Um analisador de dados do mercado imobiliário desenvolvido em Python.

O projeto realiza a coleta automática de imóveis através da API da CTI Imobiliária, processa os dados, gera análises estatísticas, exporta relatórios em diferentes formatos e cria um dashboard com visualização gráfica das principais informações.

---

## Dashboard

![Dashboard](images\Dash_print.png)

---

## Resumo no Terminal

![Terminal](images\terminal.png)

---

## Exportações

![Excel](images\ExcellPrint.png)

---

# Funcionalidades

- Coleta automática de imóveis através da API
- Paginação automática
- Tratamento de erros durante a coleta
- Estrutura modular
- Análise estatística dos imóveis
- Ranking de bairros
- Ranking de cidades
- Ranking por tipo de imóvel
- Ranking por quantidade de quartos
- Exportação para JSON
- Exportação para CSV
- Exportação para Excel
- Dashboard com gráficos
- Resumo no terminal

---

# Tecnologias

- Python
- Requests
- Pandas
- Matplotlib
- JSON

---


---

# Fluxo da Aplicação

```text
API CTI
    │
    ▼
Scraper
    │
    ▼
Analyzer
    │
    ├── Terminal
    ├── Dashboard
    └── Exportações
```

---

# Como executar

Clone o repositório:

```bash
git clone https://github.com/robertob-data/Property-Market-Analyzer.git
```

Entre na pasta:

```bash
cd Property-Market-Analyzer
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

---

# Resultados Gerados

Ao finalizar a execução, o projeto gera automaticamente:

- Dashboard em imagem (.png)
- Relatório Excel (.xlsx)
- Arquivo CSV
- Arquivo JSON
- Resumo estatístico no terminal

---

## Autor

Roberto Batista Dias

Python Developer