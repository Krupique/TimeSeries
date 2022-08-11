import numpy as np
import pandas as pd

# Pacote que fornece a API para comunicação com o Yahoo Finances
import yfinance as yf

def coletaDados(list_codigos = [], interval = '1mo', start = '2015-01-01', end='2022-01-01'):
    
    if not isinstance(list_codigos, list):
        aux = list_codigos
        list_codigos = [aux]

    if len(list_codigos) == 0:
        return 'Erro: Insira um código em empresa listada.'


    list_dfs = []
    try:
        for codigo in list_codigos:
            ticket = yf.Ticker(codigo)
            aux = ticket.history(interval=interval, start=start, end=end)
            #aux.reset_index(inplace=True)
            aux['Ticket'] = codigo

            aux = expandirDataFrame(aux)

            list_dfs.append(aux)




        return list_dfs

    except Exception as e: 
        print(e)
        return 'Erro: Erro ao ler os dados'


def expandirDataFrame(df):
    df.reset_index(inplace=True)

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Week'] = df['Date'].dt.isocalendar().week
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['YearMonth'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m'))

    dayweek_map = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday',
        4 : 'Friday',
        5 : 'Saturday',
        6 : 'Sunday'
    }

    months_map = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    df['NameMonths'] = df['Month'].map(months_map)

    df['NameDayOfWeek'] = df['DayOfWeek'].map(dayweek_map)

    return df



def agrupaDados(list_df, columns, tipo_agrupamento):
    list_res = []

    tipo_agrupamento = 'mean' if tipo_agrupamento == 'Média' else 'sum' if tipo_agrupamento == 'Somatório' else 'median' 

    for df in list_df:
        #aux_df = df.groupby(columns, as_index=False).agg([tipo_agrupamento])
        aux_df = df.groupby(columns, as_index=False).agg(tipo_agrupamento)
        list_res.append(aux_df)

    return list_res



def geraDatas(dados, dataInicial, agrupamento):
    
    quantidade = len(dados) + 1
    if agrupamento == 'Date':
        freq = 'B'
        strftime = '%Y-%m-%d'

        datas = pd.date_range(start=dataInicial, periods=quantidade, freq=freq)[1:]
        datas = pd.to_datetime(datas.strftime(strftime))

    elif agrupamento == 'Week':
        datas = []
        valor = dataInicial + 1
        for i in range(len(dados)):
            if valor > 53:
                valor = 0
            datas.append(valor)


    elif agrupamento == 'YearMonth':
        freq = 'm'
        strftime = '%Y-%m'

        datas = pd.date_range(start=dataInicial, periods=quantidade, freq=freq)[1:]
        datas = pd.to_datetime(datas.strftime(strftime))

    elif agrupamento == 'Year':
        freq = 'Y'
        strftime = '%Y'

        valor = int(dataInicial) + 1
        datas = range(valor, valor + len(dados))


    df = pd.DataFrame(dados)
    df[agrupamento] = datas
    df.columns = ['Previsões', agrupamento]

    df = df[[agrupamento, 'Previsões']]

    return df


