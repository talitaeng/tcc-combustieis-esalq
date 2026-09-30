
# 📘Business Intelligence e ciência de dados aplicados à análise da transmissão de preços dos combustíveis no Brasil

[![Power BI](https://img.shields.io/badge/Power_BI-Acessar_Dashboard-F2C94C?style=for-the-badge&logo=powerbi&logoColor=black)](https://app.powerbi.com/view?r=eyJrIjoiM2VhNmYyMjQtODJkNy00ZDYyLTg0NzktNDViZDUxMmRiNWQ0IiwidCI6IjdhNTkyOTcwLWJlNzktNGFjNS05YTI0LWY2ODNiMGI2NWZjYiJ9)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![USP Esalq](https://img.shields.io/badge/USP_Esalq-MBA_Data_Science-0055A5?style=for-the-badge)


## 📌 Sobre o Projeto
Este repositório contém o código-fonte, pipeline de dados e documentação do Trabalho de Conclusão de Curso (TCC) do MBA em **Data Science and Analytics (USP Esalq)**

O objetivo do trabalho é quantificar a capacidade explicativa e a taxa de repasse (*pass-through*) da variação do petróleo **Brent** e da taxa de câmbio (**Dólar PTAX**) sobre os preços praticados ao consumidor final no Brasil (Gasolina, Diesel S10 e Etanol) entre janeiro de 2023 e dezembro de 2025.

A solução combina um motor de engenharia e modelagem econométrica em **Python** com um painel analítico interativo em **Microsoft Power BI** baseado no modelo dimensional de Kimball (*Star Schema*)

🔗**[<font color='F2C94C'>Acessar Painel Interativo PBI Web</font>](https://app.powerbi.com/view?r=eyJrIjoiM2VhNmYyMjQtODJkNy00ZDYyLTg0NzktNDViZDUxMmRiNWQ0IiwidCI6IjdhNTkyOTcwLWJlNzktNGFjNS05YTI0LWY2ODNiMGI2NWZjYiJ9)**

---
## 📊 Fonte de Dados

Devido ao limite de tamanho do GitHub para ficheiros extensos, os dados brutos (`data/raw`) não estão incluídos diretamente neste repositório <br>
Os dados utilizados neste projeto foram obtidos a partir do portal de **Dados Abertos da ANP**

- **Série Histórica de Preços de Combustíveis:** [Série Histórica ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis)
- **Preço do Petróleo Brent - IPEA:** [Dados de Cotação do Brent](https://www.ipeadata.gov.br/Default.aspx)

### Como reproduzir:
1 - Faça o download dos arquivos dos anos de interesse (2023 a 2025) no site da ANP.<br>
2 - Salve os ficheiros .csv originais na pasta `data/raw`.<br>
3 - No site do IPEA, na barra de pesquisa procure por "Preço - petróleo bruto - Brent (FOB)" e faça o download do arquivo extensão .csv.<br>
4 - Execute o script de Processamento  `scripts/01_Processamento.py` para gerar as bases em  `data/processed`.
  
## Arquitetura da Solução

```mermaid
graph LR
    A["Fontes de Dados<br/>(ANP, BCB, Ipea, IBGE)"] --> B["Pipeline Python<br/>(Tratamento & Regressão LSDV)"]
    B --> C[("Data Mart .CSV<br/>(Star Schema Kimball)")]
    C --> D["Power BI Service<br/>(Medidas DAX & Dashboard)"]
```

##  📁 Estrutura do Repositório
``` 
├── data/
│   ├── raw/                  # Arquivos brutos baixados (ANP,  Ipea, BCB, IBGE)
│   └── processed/            # Tabelas Fato e Dimensão processadas em .csv
├── scripts/
│   ├── 01_Processamento.py     # Tratamento e unificação das bases
│   ├── 02_Modelagem.py    # Regressão LSDV e testes de Pearson
│   └── 03_Arquitetura.py            # Geração das tabelas Fato e Dimensão (Kimball)
├── dashboard/
│   └── painel_combustiveis.pbix      # Dashboard interativo do Power BI
├── .gitignore                
├── requirements.txt          # Dependências do ecossistema Python
└── README.md                 # Documentação do projeto
```

## 🛠️ Ferramentas Utilizadas
- **Linguagens & Bibliotecas:** Python (`pandas`, `numpy`, `statsmodels`, `scipy`, `yfinance`)
- **Business Intelligence:** Microsoft Power BI (Power Query, Modelagem Star Schema, Linguagem DAX)
- **IDE & Versionamento:** VS Code | Git & GitHub

## 👩🏻‍💻 Autora
**Talita Figueiredo Claro**<br>
Engenheira Química (FASB) | MBA Data Science e Analytics (USP Esalq)
