# %%
import pandas as pd 
import numpy as np 
import statsmodels.api as sm 
import scipy.stats as stats

# %%
# carregando a base de dados usada para modelagem

anp = pd.read_csv('f_anp.csv', sep=';', encoding='latin-1')
anp

# %%
# configurando a data para tipo data

anp['Data'] = pd.to_datetime(anp['Data'], dayfirst=False )

# %%
# segregando os dfs por produtos

# GASOLINA - Período 2023 a 2025

df_gasolina = anp[anp['Produto']=='GASOLINA'].copy().reset_index(drop=True)

# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 

gasolina = df_gasolina.groupby(['Ano', 'Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

gasolina['Ano'] = gasolina['Ano'].astype('category')
gasolina['Estado'] = gasolina['Estado'].astype('category')


modelo_gasolina = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado*Ano', gasolina).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(gasolina['bomba_medio'], gasolina['brent_medio']*gasolina['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(gasolina['bomba_medio'], gasolina['usd_brl'])


# Exibindo os resultados

print(modelo_gasolina.summary())
print(f' Beta modelo brent : {modelo_gasolina.params['brent_medio']:.4f} usd_brl:{modelo_gasolina.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_gasolina.pvalues['brent_medio']:.4f} usd_brl:{modelo_gasolina.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023 a 2025 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023 a 2023 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

gasolina['valor estimado'] = modelo_gasolina.fittedvalues 
gasolina['residuos modelo'] = modelo_gasolina.resid 
gasolina['Periodo analise'] = "2023-2025" 
gasolina['Produto'] = 'GASOLINA' 


# %%
# GASOLINA - Período 2023

gasolina23 = df_gasolina[df_gasolina['Ano']==2023].copy().reset_index(drop=True)
gasolina23 = gasolina23.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

gasolina23['Estado'] = gasolina23['Estado'].astype('category')


modelo_gasolina23 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', gasolina23).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(gasolina23['bomba_medio'], gasolina23['brent_medio']*gasolina23['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(gasolina23['bomba_medio'], gasolina23['usd_brl'])


# Exibindo os resultados

print(modelo_gasolina23.summary())
print(f' Beta modelo brent : {modelo_gasolina23.params['brent_medio']:.4f} usd_brl:{modelo_gasolina23.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_gasolina23.pvalues['brent_medio']:.4f} usd_brl:{modelo_gasolina23.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

gasolina23['valor estimado'] = modelo_gasolina23.fittedvalues 
gasolina23['residuos modelo'] = modelo_gasolina23.resid 
gasolina23['Periodo analise'] = "2023" 
gasolina23['Produto'] = 'GASOLINA' 


# %%
# GASOLINA - Período 2024

gasolina24 = df_gasolina[df_gasolina['Ano']==2024].copy().reset_index(drop=True)
gasolina24 = gasolina24.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

gasolina24['Estado'] = gasolina24['Estado'].astype('category')


modelo_gasolina24 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', gasolina24).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(gasolina24['bomba_medio'], gasolina24['brent_medio']*gasolina24['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(gasolina24['bomba_medio'], gasolina24['usd_brl'])


# Exibindo os resultados

print(modelo_gasolina24.summary())
print(f' Beta modelo brent : {modelo_gasolina24.params['brent_medio']:.4f} usd_brl:{modelo_gasolina24.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_gasolina24.pvalues['brent_medio']:.4f} usd_brl:{modelo_gasolina24.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2024  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2024  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

gasolina24['valor estimado'] = modelo_gasolina24.fittedvalues 
gasolina24['residuos modelo'] = modelo_gasolina24.resid 
gasolina24['Periodo analise'] = "2024" 
gasolina24['Produto'] = 'GASOLINA' 

# %%
# GASOLINA - Período 2025

gasolina25 = df_gasolina[df_gasolina['Ano']==2025].copy().reset_index(drop=True)
gasolina25 = gasolina25.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

gasolina25['Estado'] = gasolina25['Estado'].astype('category')


modelo_gasolina25 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', gasolina25).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(gasolina25['bomba_medio'], gasolina25['brent_medio']*gasolina25['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(gasolina25['bomba_medio'], gasolina25['usd_brl'])


# Exibindo os resultados

print(modelo_gasolina25.summary())
print(f' Beta modelo brent : {modelo_gasolina25.params['brent_medio']:.4f} usd_brl:{modelo_gasolina25.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_gasolina25.pvalues['brent_medio']:.4f} usd_brl:{modelo_gasolina25.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2025  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2025  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

gasolina25['valor estimado'] = modelo_gasolina25.fittedvalues 
gasolina25['residuos modelo'] = modelo_gasolina25.resid 
gasolina25['Periodo analise'] = "2025" 
gasolina25['Produto'] = 'GASOLINA' 

# %%
# segregando os dfs por produtos

# DIESEL S10 - Período 2023 a 2025

df_diesel = anp[anp['Produto']=='DIESEL S10'].copy().reset_index(drop=True)

# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 

diesel = df_diesel.groupby(['Ano', 'Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

diesel['Ano'] = diesel['Ano'].astype('category')
diesel['Estado'] = diesel['Estado'].astype('category')


modelo_diesel = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado*Ano', diesel).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(diesel['bomba_medio'], diesel['brent_medio']*diesel['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(diesel['bomba_medio'], diesel['usd_brl'])


# Exibindo os resultados

print(modelo_diesel.summary())
print(f' Beta modelo brent : {modelo_diesel.params['brent_medio']:.4f} usd_brl:{modelo_diesel.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_diesel.pvalues['brent_medio']:.4f} usd_brl:{modelo_diesel.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023 a 2025 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023 a 2023 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

diesel['valor estimado'] = modelo_diesel.fittedvalues 
diesel['residuos modelo'] = modelo_diesel.resid 
diesel['Periodo analise'] = "2023-2025" 
diesel['Produto'] = 'DIESEL S10' 


# %%
# segregando os dfs por produtos

# DIESEL S10 - Período 2023 

diesel23 = df_diesel[df_diesel['Ano']==2023].copy().reset_index(drop=True)

diesel23 = diesel23.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

diesel23['Estado'] = diesel23['Estado'].astype('category')


modelo_diesel23 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', diesel23).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(diesel23['bomba_medio'], diesel23['brent_medio']*diesel23['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(diesel23['bomba_medio'], diesel23['usd_brl'])


# Exibindo os resultados

print(modelo_diesel23.summary())
print(f' Beta modelo brent : {modelo_diesel23.params['brent_medio']:.4f} usd_brl:{modelo_diesel23.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_diesel23.pvalues['brent_medio']:.4f} usd_brl:{modelo_diesel23.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

diesel23['valor estimado'] = modelo_diesel23.fittedvalues 
diesel23['residuos modelo'] = modelo_diesel23.resid 
diesel23['Periodo analise'] = "2023" 
diesel23['Produto'] = 'DIESEL S10' 

# %%
# DIESEL S10 - Período 2024 

diesel24 = df_diesel[df_diesel['Ano']==2024].copy().reset_index(drop=True)

diesel24 = diesel24.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

diesel24['Estado'] = diesel24['Estado'].astype('category')


modelo_diesel24 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', diesel24).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(diesel24['bomba_medio'], diesel24['brent_medio']*diesel24['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(diesel24['bomba_medio'], diesel24['usd_brl'])


# Exibindo os resultados

print(modelo_diesel24.summary())
print(f' Beta modelo brent : {modelo_diesel24.params['brent_medio']:.4f} usd_brl:{modelo_diesel24.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_diesel24.pvalues['brent_medio']:.4f} usd_brl:{modelo_diesel24.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2024  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2024  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

diesel24['valor estimado'] = modelo_diesel24.fittedvalues 
diesel24['residuos modelo'] = modelo_diesel24.resid 
diesel24['Periodo analise'] = "2024" 
diesel24['Produto'] = 'DIESEL S10'

# %%
# DIESEL S10 - Período 2025 

diesel25 = df_diesel[df_diesel['Ano']==2025].copy().reset_index(drop=True)

diesel25 = diesel25.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

diesel25['Estado'] = diesel25['Estado'].astype('category')


modelo_diesel25 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', diesel25).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(diesel25['bomba_medio'], diesel25['brent_medio']*diesel25['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(diesel25['bomba_medio'], diesel25['usd_brl'])


# Exibindo os resultados

print(modelo_diesel25.summary())
print(f' Beta modelo brent : {modelo_diesel25.params['brent_medio']:.4f} usd_brl:{modelo_diesel25.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_diesel25.pvalues['brent_medio']:.4f} usd_brl:{modelo_diesel25.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2025  correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2025  correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

diesel25['valor estimado'] = modelo_diesel25.fittedvalues 
diesel25['residuos modelo'] = modelo_diesel25.resid 
diesel25['Periodo analise'] = "2025" 
diesel25['Produto'] = 'DIESEL S10'

# %%

# ETANOL - Período 2023 a 2025

df_etanol = anp[anp['Produto']=='ETANOL'].copy().reset_index(drop=True)

# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 

etanol = df_etanol.groupby(['Ano', 'Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

etanol['Ano'] = etanol['Ano'].astype('category')
etanol['Estado'] = etanol['Estado'].astype('category')


modelo_etanol = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado*Ano', etanol).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(etanol['bomba_medio'], etanol['brent_medio']*etanol['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(etanol['bomba_medio'], etanol['usd_brl'])


# Exibindo os resultados

print(modelo_etanol.summary())
print(f' Beta modelo brent : {modelo_etanol.params['brent_medio']:.4f} usd_brl:{modelo_etanol.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_etanol.pvalues['brent_medio']:.4f} usd_brl:{modelo_etanol.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023 a 2025 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023 a 2023 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

etanol['valor estimado'] = modelo_etanol.fittedvalues 
etanol['residuos modelo'] = modelo_etanol.resid 
etanol['Periodo analise'] = "2023-2025" 
etanol['Produto'] = 'ETANOL' 


# %%
# ETANOL - Período 2023 


# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 
etanol23 = df_etanol[df_etanol['Ano']==2023].copy().reset_index(drop=True)
etanol23 = etanol23.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

etanol23['Estado'] = etanol23['Estado'].astype('category')


modelo_etanol23 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', etanol23).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(etanol23['bomba_medio'], etanol23['brent_medio']*etanol23['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(etanol23['bomba_medio'], etanol23['usd_brl'])


# Exibindo os resultados

print(modelo_etanol23.summary())
print(f' Beta modelo brent : {modelo_etanol23.params['brent_medio']:.4f} usd_brl:{modelo_etanol23.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_etanol23.pvalues['brent_medio']:.4f} usd_brl:{modelo_etanol23.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2023 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2023 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

etanol23['valor estimado'] = modelo_etanol23.fittedvalues 
etanol23['residuos modelo'] = modelo_etanol23.resid 
etanol23['Periodo analise'] = "2023" 
etanol23['Produto'] = 'ETANOL'

# %%
# ETANOL - Período 2024 


# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 
etanol24 = df_etanol[df_etanol['Ano']==2024].copy().reset_index(drop=True)
etanol24 = etanol24.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

etanol24['Estado'] = etanol24['Estado'].astype('category')


modelo_etanol24 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', etanol24).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(etanol24['bomba_medio'], etanol24['brent_medio']*etanol24['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(etanol24['bomba_medio'], etanol24['usd_brl'])


# Exibindo os resultados

print(modelo_etanol24.summary())
print(f' Beta modelo brent : {modelo_etanol24.params['brent_medio']:.4f} usd_brl:{modelo_etanol24.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_etanol24.pvalues['brent_medio']:.4f} usd_brl:{modelo_etanol24.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2024 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2024 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

etanol24['valor estimado'] = modelo_etanol24.fittedvalues 
etanol24['residuos modelo'] = modelo_etanol24.resid 
etanol24['Periodo analise'] = "2024" 
etanol24['Produto'] = 'ETANOL'

# %%
# ETANOL - Período 2025 


# empregando agrupamento de Ano, Quinzena e Estado para Estimar o modelo 
etanol25 = df_etanol[df_etanol['Ano']==2025].copy().reset_index(drop=True)
etanol25 = etanol25.groupby(['Quinzena', 'Estado']).agg( 
    bomba_medio = ('Valor do produto', 'mean'),  
    brent_medio = ('valor brent', 'mean'),  
    usd_brl = ('valor cotacao', 'mean') 
    ).round(3).reset_index() 

etanol25['Estado'] = etanol25['Estado'].astype('category')


modelo_etanol25 = sm.OLS.from_formula('bomba_medio ~ brent_medio + usd_brl + Estado', etanol25).fit()

# correlação com o brent em R$
corr_r, p_value = stats.pearsonr(etanol25['bomba_medio'], etanol25['brent_medio']*etanol25['usd_brl'])

# correlação com o dólar
corr_rd, p_valued = stats.pearsonr(etanol25['bomba_medio'], etanol25['usd_brl'])


# Exibindo os resultados

print(modelo_etanol25.summary())
print(f' Beta modelo brent : {modelo_etanol25.params['brent_medio']:.4f} usd_brl:{modelo_etanol25.params['usd_brl']:.4f}')
print(f' p_value modelo brent : {modelo_etanol25.pvalues['brent_medio']:.4f} usd_brl:{modelo_etanol25.pvalues['usd_brl']:.4f}')
print(f' Período de Analise 2025 correlação (r): {corr_r:.4f} p_value P {p_value:.4f}' )
print(f' Período de Analise 2025 correlação (r): {corr_rd:.4f} p_value P {p_valued:.4f}')

# Armazenado os resultados estimados e os resíduos no df, com acrescimo da coluna Periodo_Analise que servirá como identificador 
# do periodo para o fitted gerados 

etanol25['valor estimado'] = modelo_etanol25.fittedvalues 
etanol25['residuos modelo'] = modelo_etanol25.resid 
etanol25['Periodo analise'] = "2025" 
etanol25['Produto'] = 'ETANOL'

# %%
# Unindo os dfs com os fitted gerados

lista_df = [
    gasolina, gasolina23, gasolina24, gasolina25,
    diesel, diesel23, diesel24, diesel25,
    etanol, etanol23, etanol24, etanol25
]

f2_fittedvalues = pd.concat(lista_df, ignore_index=True)
f2_fittedvalues = pd.DataFrame(f2_fittedvalues)

f2_fittedvalues.to_csv('fittedvalues.csv', sep=';', encoding='latin-1', index=False)

# %%
# Armazenando as métricas do modelo

lista_modelos = []

def ad_modelo (df, modelo, nome_produto, periodo):
    corr_r, p_value = stats.pearsonr(df['bomba_medio'], df['brent_medio']*df['usd_brl']) 
    corr_rd, p_valued = stats.pearsonr(df['bomba_medio'],df['usd_brl'])  
    dados_modelo = { 
        'Produto': nome_produto, 
        'Periodo Analise': periodo, 
        'R²': round(modelo.rsquared, 4), 
        'R² Adj.': round(modelo.rsquared_adj, 4), 
        'F-statistic': round(modelo.fvalue, 4), 
        'Prob-f': round(modelo.f_pvalue, 4), 
        'Observações': int(modelo.nobs), 
        'GL - Modelo' : int(modelo.df_model), 
        'GL - Residuo' : int(modelo.df_resid), 
        'Coef Brent US$ β₀' : round(modelo.params['brent_medio'], 4), 
        'p_value β₀': round(modelo.pvalues['brent_medio'],4), 
        ' Coef Dolar US$_BRL β₁': round(modelo.params['usd_brl'], 4), 
        'p_value β₁': round(modelo.pvalues['usd_brl'],4), 
        'correlação (r) brent' : round(corr_r,4), 
        'p-valor brent' : round(p_value,4), 
        'correlação (r) dolar' : round(corr_rd,4), 
        'p-valor dolar' : round(p_valued,4), 
    } 
    lista_modelos.append(dados_modelo) 

# %%
# Adicionando os resultados
ad_modelo(gasolina, modelo_gasolina, 'GASOLINA', '2023-2025')
ad_modelo(gasolina23, modelo_gasolina23, 'GASOLINA', '2023')
ad_modelo(gasolina24, modelo_gasolina24, 'GASOLINA', '2024')
ad_modelo(gasolina25, modelo_gasolina25, 'GASOLINA', '2025')


ad_modelo(diesel, modelo_diesel, 'DIESEL S10', '2023-2025')
ad_modelo(diesel23, modelo_diesel23, 'DIESEL S10', '2023')
ad_modelo(diesel24, modelo_diesel24, 'DIESEL S10', '2024')
ad_modelo(diesel25, modelo_diesel25, 'DIESEL S10', '2025')


ad_modelo(etanol, modelo_etanol, 'ETANOL', '2023-2025')
ad_modelo(etanol23, modelo_etanol23, 'ETANOL', '2023')
ad_modelo(etanol24, modelo_etanol24, 'ETANOL', '2024')
ad_modelo(etanol25, modelo_etanol25, 'ETANOL', '2025')

# %%
df_metricas = pd.DataFrame(lista_modelos)
df_metricas.to_csv('metricas_modelo.csv', sep=';', encoding='utf-8', index=False)


