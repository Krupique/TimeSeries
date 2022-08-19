import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from numpy import abs



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

def decomporSerie(df, type, column):
    decomposicao = seasonal_decompose(df[['Close']], period=50, model = type, extrapolate_trend = 'freq')


    dfTrend = pd.DataFrame(decomposicao.trend).reset_index()
    dfTrend.name = 'Tendência'
    dfTrend.columns = [column, 'Value']
    dfTrend[column] = df[column]

    dfSazonal = pd.DataFrame(decomposicao.seasonal).reset_index()
    dfSazonal.name = 'Sazonalidade'
    dfSazonal.columns = [column, 'Value']
    dfSazonal[column] = df[column]
    
    dfResid = pd.DataFrame(decomposicao.resid).reset_index()
    dfResid.name = 'Resíduos'
    dfResid.columns = [column, 'Value']
    dfSazonal[column] = df[column]

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

def calculaDesvioPadrao(df, days = 30):
    df['DesvioPadrao'] = df['Close'].rolling(window = days).std()

    return df


def currencyFormatting(value):
    neg = '-' if value < 0 else '' 
    value = abs(value)

    if value / 1000000000 > 1:
        return f'{neg}$ {str(round(value/1000000000, 2))}B'
    elif value / 1000000 > 1:
        return f'{neg}$ {str(round(value/1000000, 2))}M'
    elif value / 100000 > 1:
        return f'{neg}$ {str(round(value/100000, 2))}KK'
    elif value / 1000 > 1:
        return f'{neg}$ {str(round(value/10000, 2))}k'
    else: 
        return f'{neg}$ {str(round(value, 2))}'

