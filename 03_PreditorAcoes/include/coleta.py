import numpy as np
import pandas as pd
import datetime

# Pacote que fornece a API para comunicação com o Yahoo Finances
import yfinance as yf

def coletaDados(list_codigos = [], interval = '1mo', start = '2015-01-01', end='2022-01-01'):
    print('Iniciou a coleta dos dados...')

    df_info = pd.DataFrame()
    
    if not isinstance(list_codigos, list):
        aux = list_codigos
        list_codigos = [aux]

    if len(list_codigos) == 0:
        return 'Erro: Insira um código de uma empresa listada.'

    list_columns_info = ['shortName', 'longName', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'country', 'industry', 'financialCurrency',
                    'recommendationKey', 'recommendationMean', 'currentPrice', 'earningsGrowth', 'currentRatio', 'returnOnAssets', 'numberOfAnalystOpinions',
                    'targetMeanPrice', 'market', 'website', 'logo_url',
                    ]
    list_columns_news = ['title', 'publisher', 'providerPublishTime', 'link']

    
    list_dfs = []
    list_dfs_quartfinancials = []
    list_dfs_sustainability = []
    list_dfs_news = []
    try:
        list_rows_info = []
        for codigo in list_codigos:
            ticket = yf.Ticker(codigo)
            aux = ticket.history(interval=interval, start=start, end=end)
            #aux.reset_index(inplace=True)
            aux['Ticket'] = codigo

            aux = expandirDataFrame(aux)
            aux.dropna(inplace=True)

            list_dfs.append(aux)


            # Info
            info = ticket.info
            list_values_info = []
            for column in list_columns_info:
                list_values_info.append(info[column])

            list_rows_info.append(list_values_info)

        
            # Quarterly Financials
            quarterly_financials = ticket.quarterly_financials
            aux = quarterly_financials.T[['Gross Profit', 'Net Income', 'Total Revenue']]

            list_dfs_quartfinancials.append(aux)
                    
        
        
            # Sustainability
            sustainability = ticket.sustainability
            aux = sustainability.T[['socialScore', 'governanceScore', 'environmentScore', 'totalEsg']]

            list_dfs_sustainability.append(aux)


            # News
            news = ticket.news
            list_rows_news = []
            for i in range(len(news)):

                list_values_news = []
                for column in list_columns_news:
                    list_values_news.append(news[i][column])

                list_rows_news.append(list_values_news)
            
            aux = pd.DataFrame(list_rows_news, columns=list_columns_news)

            aux['date'] = aux['providerPublishTime'].apply(timeStampToDate)
            list_dfs_news.append(aux)
        
        #Criando DataFrame de Info
        df_info = pd.DataFrame(list_rows_info, columns=list_columns_info, index=list_codigos)




        return df_info, list_dfs, list_dfs_quartfinancials, list_dfs_sustainability, list_dfs_news

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
    df['Data'] = df['Date'].dt.strftime('%Y/%m/%d')
    


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
        if columns[0] == 'YearMonth':
            aux_df['Year Month'] = aux_df['YearMonth'].dt.strftime('%Y/%m')
        list_res.append(aux_df)




    return list_res



def geraDatas(dados, dataInicial, agrupamento):
    
    quantidade = len(dados) + 1
    if agrupamento == 'Date':
        freq = 'B'
        strftime = '%Y-%m-%d'

        datas = pd.date_range(start=dataInicial, periods=quantidade, freq=freq)[1:]
        datas = pd.to_datetime(datas.strftime(strftime))
        
        
        strftime = '%Y/%m/%d'
        datas_display = datas.strftime(strftime)

    elif agrupamento == 'Week':
        datas = []
        valor = dataInicial + 1
        for i in range(len(dados)):
            if valor > 53:
                valor = 0
            datas.append(valor)

        datas_display = datas

    elif agrupamento == 'YearMonth':
        freq = 'm'
        strftime = '%Y-%m'

        datas = pd.date_range(start=dataInicial, periods=quantidade, freq=freq)[1:]
        datas = pd.to_datetime(datas.strftime(strftime))

        strftime = '%Y/%m'
        datas_display = datas.strftime(strftime)

    elif agrupamento == 'Year':
        freq = 'Y'
        strftime = '%Y'

        valor = int(dataInicial) + 1
        datas = range(valor, valor + len(dados))

        datas_display = datas


    df = pd.DataFrame(dados)
    df[agrupamento] = datas
    df['Data'] = datas_display

    df.columns = ['Valores Previstos', agrupamento, 'Data']

    df = df[[agrupamento, 'Valores Previstos', 'Data']]

    return df


def timeStampToDate(value):
    try:
        date = datetime.datetime.fromtimestamp(value)
        resultado = f'{date.year}/{date.month}/{date.day} {date.hour}:{date.minute}'
        return resultado

    except:
        return '-'
