
Este arquivo apresenta algumas medidas que foram necessárias para a viabilização da interação e navegações nos painéis de Business Inteligence, não serão apresentadas todas as medidas, apenas aquelas com contexto de filtro elaborado e condicionais. Em grande maioria, as medidas criadas fazem parte do contexto geral utilizando CALCULATE, AVERAGE, MIN, MAX. A medida apresentada abaixo, permitiu realizar busca inteligente para todos os valores desejados, portanto, mudou-se apenas o valor de interesse na busca.
    
```
    p-valor P Brent =
    VAR Produtoselecionado = SELECTEDVALUE(d_produto[Produto])
    VAR Anosel = SELECTEDVALUE(d_calendario[Ano])
    VAR geral = "2023-2025"
    RETURN
    IF(
    ISBLANK(Produtoselecionado),
    " ",
    IF(
    ISBLANK(Anosel),
    LOOKUPVALUE(f2_metricas_modelo[p-valor brent],
    d_produto[Produto], Produtoselecionado,
    f2_metricas_modelo[Periodo Analise], geral),
    LOOKUPVALUE(f2_metricas_modelo[p-valor brent],
    d_produto[Produto], Produtoselecionado,
    f2_metricas_modelo[Periodo Analise], FORMAT(Anosel, "0"))
    )
    )
```

Medida criada para localizar região de maior e menor valor através de tabela virtual utilizando SUMMARIZE

    Região de Maior Valor =
        VAR TabelaRegiao = 
            SUMMARIZE(d_regiao, d_regiao[Nome Estado],
            "Média",
            [Bomba R$ Méd]) 
        VAR MaiorValor = MAXX(TabelaRegiao,[Média])
        VAR NomeRegiao = SELECTCOLUMNS(TOPN(1,TabelaRegiao,[Média],
        DESC),"Nome", d_regiao[Nome Estado])
        RETURN
        NomeRegiao & " " & FORMAT(MaiorValor, "R$ #,##0.00") & " "
    

     Região de menor Valor =
        VAR TabelaRegiao =
            SUMMARIZE(d_regiao, d_regiao[Nome Estado],
            "Média", 
            [Bomba R$ Méd])
        VAR MaiorValor = MINX(TabelaRegiao,[Média])
        VAR NomeRegiao = SELECTCOLUMNS(TOPN(1,TabelaRegiao,[Média],
        ASC),"Nome", d_regiao[Nome Estado])
        RETURN
        NomeRegiao & " " & FORMAT(MaiorValor, "R$ #,##0.00") & " "