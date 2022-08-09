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



def agrupaDados(list_df, columns):
    list_res = []

    for df in list_df:
        aux_df = df.groupby(columns, as_index=False).sum()
        list_res.append(aux_df)

    return list_res


