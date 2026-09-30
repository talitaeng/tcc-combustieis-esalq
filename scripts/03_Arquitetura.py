# %%
import pandas as pd 
import numpy as np 


# %%
# Criando tabela dimensão produto

produtos = {
    'Produto': ['GASOLINA', 'ETANOL', 'DIESEL S10'],
    'ID Produto': [1,2,3]
}

df_produto = pd.DataFrame(produtos)
df_produto.to_csv('d_produto.csv', sep=';', encoding='latin-1', index=False)

# %%
# criando a dimensao região a partir da API do IBGE

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?view=nivelado"
ibge = pd.read_json(url)
ibge

# %%
ibge = ibge.rename(columns={
    'UF-id': 'ID Estado',
    'UF-sigla': 'UF', 
    'UF-nome':'Nome Estado', 
    'regiao-sigla': 'Regiao', 
    'regiao-nome': 'Nome Regiao'
})

ibge = ibge.drop(columns='regiao-id')

# %%
ibge.to_csv('d_regiao.csv', sep=';', encoding='latin-1', index=False)

# %%
# exportar a base ANP para atribuir quantas bandeiras de postos revendedores existem

anp = pd.read_csv('f_anp.csv', sep=';', encoding='latin-1')
anp

# %%
bandeiras = list(anp['Bandeira'].unique())

df_bandeira = pd.DataFrame({
    'ID Bandeira' : range(1, len(bandeiras) + 1),
    'Bandeira': bandeiras
})

# %%
df_bandeira

# %%
# unindo df da ANP com cada id criado

# Produto

anp = pd.merge(anp, df_produto, on='Produto', how='inner')


# %%
# Estado

anp = pd.merge(anp, ibge, 
left_on='Estado',
right_on='UF', 
how='left')

anp

# %%
anp = pd.merge(anp, df_bandeira, on='Bandeira', how='left')

# %%
anp

# %%
# salvando a tabela fato ANP apenas com os identificadores

anp = anp[['Data', 'Ano','Quinzena', 'ID Produto', 'ID Estado', 'ID Bandeira', 'Valor do produto', 'valor brent', 'Paridade', 'valor cotacao']]
anp.to_csv('f_anp_2023a2025.csv', sep=';', encoding='latin-1', index=False)

# %%
# tratando a dimensão Bandeira

df_bandeira['Bandeira'] = df_bandeira['Bandeira'].str.capitalize()


# %%
df_bandeira

# %%
df_bandeira.to_csv('d_bandeira.csv', sep=';', encoding='utf-8', index=False)

# %%
# criando a dimensão calendario para o intervalo de datas da ANP

anp['Data'] = pd.to_datetime(anp['Data'], dayfirst=False)
print(anp['Data'].min())
print(anp['Data'].max())

# %%
datamin = anp['Data'].min()
datamax = anp['Data'].max()
datas = pd.date_range(start=datamin, end=datamax)

dCalendario = pd.DataFrame({'Data': datas})
dCalendario

# %%
dCalendario['Ano'] = dCalendario['Data'].dt.year
dCalendario['Mês'] = dCalendario['Data'].dt.month
dCalendario['Nome Mês'] = dCalendario['Data'].dt.month_name(locale='pt_BR')
dCalendario['Dia do Ano'] = dCalendario['Data'].dt.day_of_year
dCalendario['Quinzena'] = ((dCalendario['Dia do Ano'] - 1) // 14 + 1).clip(upper=26)

# %%
dCalendario.to_csv('d_calendario.csv', sep=';', encoding='latin-1', index=False)

# %%
# configurando as tabelas fatos secundárias com o id

fitted = pd.read_csv('fittedvalues.csv', sep=';', encoding='latin-1')

# %%
fitted

# %%
fitted = pd.merge(fitted, df_produto, on='Produto', how='left')
fitted

# %%
fitted = pd.merge(fitted, ibge, left_on='Estado', right_on='UF', how='left')
fitted

# %%
fitted = fitted[['Ano', 'Quinzena', 'ID Estado', 'ID Produto','bomba_medio', 'brent_medio', 'usd_brl', 'valor estimado', 'residuos modelo', 'Periodo analise' ]]
fitted.to_csv('f2_fittedvalues.csv')

# %%
metricas = pd.read_csv('metricas_modelo.csv', sep=';', encoding='utf-8')
metricas

# %%
metricas = pd.merge(metricas, df_produto, on='Produto', how='left')


# %%
metricas.columns

# %%
metricas = metricas[['ID Produto', 'Periodo Analise', 'R²', 'R² Adj.', 'F-statistic', 'Prob-f',
       'Observações', 'GL - Modelo', 'GL - Residuo', 'Coef Brent US$ β₀',
       'p_value β₀', ' Coef Dolar US$_BRL β₁', 'p_value β₁',
       'correlação (r) brent', 'p-valor brent', 'correlação (r) dolar',
       'p-valor dolar']]

metricas

# %%
metricas.to_csv('f2_metricas_modelo.csv', sep=';', encoding='utf-8', index=False)


