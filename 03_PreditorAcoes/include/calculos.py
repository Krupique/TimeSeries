import pandas as pd
# Computação estatística
from statsmodels.tsa.seasonal import seasonal_decompose
# Imports análise e modelagem de séries temporais
from statsmodels.tsa.stattools import adfuller



def calculaRentabilidade(list_dfs, list_tickers):
    list_rentabilidade_sum = []
    list_rentabilidade_mean = []

    for df in list_dfs:
        df[['Rentability']] = df[['Close']] / df[['Close']].shift() * 100 - 100
        list_rentabilidade_sum.append(round(df['Rentability'].sum(), 3))
        list_rentabilidade_mean.append(round(df['Rentability'].mean(), 3))

    df_rentabilidade = pd.DataFrame(data=list_rentabilidade_sum, columns=['Somatório'])
    df_rentabilidade['Média'] = list_rentabilidade_mean
    df_rentabilidade.index = list_tickers

    return df_rentabilidade

def decompor_serie(df, type):
    decomposicao = seasonal_decompose(df[['Close']], period=50, model = type, extrapolate_trend = 'freq')


    dfTrend = pd.DataFrame(decomposicao.trend).reset_index()
    dfTrend.name = 'Tendência'
    dfTrend.columns = ['Date', 'Value']
    dfTrend['Date'] = df['Date']

    dfSazonal = pd.DataFrame(decomposicao.seasonal).reset_index()
    dfSazonal.name = 'Sazonalidade'
    dfSazonal.columns = ['Date', 'Value']
    dfSazonal['Date'] = df['Date']
    
    dfResid = pd.DataFrame(decomposicao.resid).reset_index()
    dfResid.name = 'Resíduos'
    dfResid.columns = ['Date', 'Value']
    dfSazonal['Date'] = df['Date']

    list_df_decomposition = [dfTrend, dfSazonal, dfResid]

    return list_df_decomposition


def calculaEstacionaridade(df, column):
    
    # Teste
    dfteste = adfuller(df[column], autolag = 'AIC')

    # Formatando a saída
    dfsaida = pd.Series(dfteste[0:4], index = ['Estatística do Teste',
                                               'Valor-p',
                                               'Número de Lags Consideradas',
                                               'Número de Observações Usadas'])

    # Loop por cada item da saída do teste
    for key, value in dfteste[4].items():
        dfsaida['Valor Crítico (%s)'%key] = value


    dfsaida = pd.DataFrame(dfsaida)
    dfsaida.index.name = 'Estatísticas'
    dfsaida.columns = ['Resultados']

    return dfsaida


def calculaMediaMovel(df, days = 7):
    df['MediaMovel'] = df['Close'].rolling(window = days).mean()

    return df