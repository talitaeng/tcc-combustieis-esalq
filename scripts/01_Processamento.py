# %%
import pandas as pd 
import numpy as np 
from glob import glob

# %%
palavra = 'Preços semestrais'
regra_de_busca = f'*{palavra}*.csv'
arquivos_selecionados = glob(regra_de_busca)

# %%
print(f'Foram encontrados {len(arquivos_selecionados)} arquivos')
print(arquivos_selecionados)

# %%
dados_anp = (pd.read_csv(arq, delimiter=';', encoding='latin-1') for arq in arquivos_selecionados)

df_anp = pd.concat(dados_anp, ignore_index=True)

# %%
df_anp

# %%
df_anp.info(show_counts=True)

# %%
# Renomeando as colunas

df_anp = df_anp.rename(columns={
    'ï»¿Regiao - Sigla': 'Regiao',
    'Estado - Sigla': 'Estado',
    'Data da Coleta' : 'Data', 
    'Valor de Venda' : 'Valor do produto',
})

df_anp

# %%
# Deixando apenas as colunas de interesse
df_anp = df_anp[['Regiao', 'Estado', 'Municipio', 'Bandeira','Produto', 'Data', 'Valor do produto']]
df_anp

# %%
# Verificando os produtos presentes no dataset

df_anp['Produto'].unique()

# %%
# Produtos escolhidos para análise: GASOLINA, ETANOL, DIESEL S10

produtos = ['ETANOL', 'GASOLINA', 'DIESEL S10']

df_anp = df_anp[df_anp['Produto'].isin(produtos)].copy().reset_index(drop=True)

# %%
df_anp

# %%
# alterando tipo data e float para as colunas de data e valor do produto

df_anp['Data'] = pd.to_datetime(df_anp['Data'], dayfirst=True)
df_anp['Valor do produto'] = df_anp['Valor do produto'].str.replace(',','.').astype(float)

# %%
df_anp

# %%
# inclusão de colunas auxiliares Dia do ano e Quinzena (atribuido como quinzena 14 dias fechados para não haver disproporção temporal entre meses de 28, 30 e 31 dias)

df_anp['Dia do Ano'] = df_anp['Data'].dt.day_of_year
df_anp['Ano'] = df_anp['Data'].dt.year

# %%
df_anp['Quinzena'] = (((df_anp['Dia do Ano']-1) // 14) + 1).clip(upper=26)

# %%
df_anp

# %%
# Confirmando a data mais antiga e a mais recente do df

datamin = df_anp['Data'].min()
datamax = df_anp['Data'].max()

# %% [markdown]
# ### Importando os dados Brent

# %%
import yfinance as yf

# %%
dados_brent = yf.download('BZ=F', start=datamin, end=datamax, multi_level_index=False)
dados_brent

# %%
# Utilizando apenas as coluna de data e valor de fechamento no mercado

df_brent = dados_brent.reset_index()
df_brent = df_brent[df_brent.columns[0:2]]
df_brent = df_brent.rename(columns={'Date': 'Data'})
df_brent

# %%
# importando os dados BRENT do Ipea Data

brent_ipea = pd.read_csv('ipeadata[02-09-2026-03-29].csv', sep=';', encoding='latin-1')
brent_ipea

# %%
brent_ipea = brent_ipea.rename(columns={
    brent_ipea.columns[0] : 'Data', 
    brent_ipea.columns[1]: 'Valor Brent'
})
brent_ipea

# %%
brent_ipea['Data'] = pd.to_datetime(brent_ipea['Data'], dayfirst=True)
brent_ipea = brent_ipea[['Data','Valor Brent']]
brent_ipea

# %%
brent_ipea = brent_ipea[(brent_ipea['Data']>= datamin)&(brent_ipea['Data']<=datamax)].copy().reset_index(drop=True)
brent_ipea

# %%
brent = pd.merge(df_brent, brent_ipea, on='Data', how='inner')

# %%
brent

# %%
brent =brent.dropna()
brent

# %%
brent['Valor Brent'] = brent['Valor Brent'].str.replace(',', '.').astype(float)

# %%
brent['valor brent'] = round(brent[['Valor Brent', 'Close']].mean(axis=1),3)
brent

# %%
brent = brent[['Data', 'valor brent']]
brent

# %%
df_anp = pd.merge(df_anp, brent, on='Data', how='inner')

# %%
df_anp

# %% [markdown]
# ### Importação dos valores e cotação dólar

# %%
url_dolar = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='USD'&@dataInicial='01-01-2023'&@dataFinalCotacao='12-31-2025'&$top=10000&$format=json&$select=paridadeVenda,cotacaoVenda,dataHoraCotacao"
dados_dolar = pd.read_json(url_dolar)
dados_dolar

# %%
dados_dolar = list(dados_dolar[dados_dolar.columns[1]])

# %%
df_dolar = pd.DataFrame(dados_dolar)
df_dolar

# %%
df_dolar.columns = ['Paridade', 'valor cotacao', 'Data']
df_dolar = df_dolar[['Data', 'Paridade', 'valor cotacao']]
df_dolar

# %%
# removendo a informação de horário da coluna para ficar apenas com as datas
df_dolar['Data'] = pd.to_datetime(df_dolar['Data'], dayfirst=False).dt.date
df_dolar

# %%
# removendo as duplicatas dos das ( extraindo a informação de fechamento )
df_bcb = df_dolar.drop_duplicates(subset=['Data'], keep='last').copy().reset_index(drop=True)
df_bcb

# %%
df_bcb['Data'] = pd.to_datetime(df_bcb['Data'], dayfirst=False)

# %%
# unindo as informações de cotação do dolar ao df_anp

df_anp = pd.merge(df_anp, df_bcb, on='Data', how='inner')


# %%
df_anp = df_anp.sort_values(by='Data').reset_index(drop=True)
df_anp

# %%
print(df_anp['Data'].min())
print(df_anp['Data'].max())

# %%
df_anp.to_csv('f_anp.csv', sep=';', encoding='utf-8', index=False)


