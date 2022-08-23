import datetime
import pandas as pd


# Pacote que fornece a API para comunicação com o Yahoo Finances
import yfinance as yf

def coletaDados(list_codigos = [], interval = '1mo', start = '2015-01-01', end='2022-01-01'):
    print('INICIOU COLETA DOS DADOS')

    df_info = pd.DataFrame()
    
    if not isinstance(list_codigos, list):
        aux = list_codigos
        list_codigos = [aux]

    if len(list_codigos) == 0:
        return 'Erro: Insira um código de uma empresa listada.'

    # Lista de atributos que serão trazidos da API no objeto Info
    list_columns_info = ['shortName', 'longName', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'country', 'industry', 'financialCurrency',
                    'recommendationKey', 'recommendationMean', 'currentPrice', 'earningsGrowth', 'currentRatio', 'returnOnAssets', 'numberOfAnalystOpinions',
                    'targetMeanPrice', 'market', 'website', 'logo_url',
                    ]

    # Lista de atributos que serão trazidos da API para o objeto News 
    list_columns_news = ['title', 'publisher', 'providerPublishTime', 'link']

    
    list_dfs_stock = []
    list_dfs_quartfinancials = []
    list_dfs_sustainability = []
    list_dfs_news = []
    try:
        list_rows_info = []
        for codigo in list_codigos:
            print(f'Coletando dados do ticker: {codigo}')
            print(f'Coletando histórico de ações...')
            

            # Busca o histórico de ações
            ticket = yf.Ticker(codigo)
            aux = ticket.history(interval=interval, start=start, end=end)
            aux['Ticket'] = codigo

            aux = expandirDataFrame(aux)
            aux.dropna(inplace=True)

            list_dfs_stock.append(aux)


            # Busca as informações
            print(f'Coletando informações adicionais...')

            info = ticket.info
            aux = pd.DataFrame()
            if ticket.info is not None:
                list_values_info = []
                for column in list_columns_info:
                    if column in info.keys():
                        list_values_info.append(info[column])
                    else:
                        list_values_info.append('None')

                list_rows_info.append(list_values_info)

            
                # Quarterly Financials
                print(f'Coletando histórico dos últimos trimestres...')

                quarterly_financials = ticket.quarterly_financials
                aux = quarterly_financials.T[['Gross Profit', 'Net Income', 'Total Revenue']]

            list_dfs_quartfinancials.append(aux)
                    
        
        
            # Sustainability
            print(f'Coletando informações de sustentabilidade...')

            sustainability = ticket.sustainability
            aux = pd.DataFrame()
            if sustainability is not None:
                aux = sustainability.T[['socialScore', 'governanceScore', 'environmentScore', 'totalEsg']]

            list_dfs_sustainability.append(aux)


            # News
            print(f'Coletando últimas notícias...')

            news = ticket.news
            aux = pd.DataFrame()
            if news is not None:
                list_rows_news = []
                for i in range(len(news)):

                    list_values_news = []
                    for column in list_columns_news:

                        if column in news[i].keys():
                            list_values_news.append(news[i][column])
                        else:
                            list_values_news.append('None')

                    list_rows_news.append(list_values_news)
                
                aux = pd.DataFrame(list_rows_news, columns=list_columns_news)

                aux['date'] = aux['providerPublishTime'].apply(timeStampToDate)

            
            list_dfs_news.append(aux)


            print(f'Coleta do ticker {codigo} concluída.\n############################')
        
        #Criando DataFrame de Info
        df_info = pd.DataFrame(list_rows_info, columns=list_columns_info, index=list_codigos)




        return df_info, list_dfs_stock, list_dfs_quartfinancials, list_dfs_sustainability, list_dfs_news

    except Exception as e: 
        print(e)
        return 'Erro: Erro ao ler os dados'

#Essa função recebe o dataframe com a coluna Date, e aplica a Granularidade na informação, quebrando ela em várias outras informações
def expandirDataFrame(df):
    df.reset_index(inplace=True)

    df['Year'] = df['Date'].dt.year #Criação do atributo Year
    df['Month'] = df['Date'].dt.month #Criação do atributo Month 
    df['Day'] = df['Date'].dt.day #Criação do atributo Day
    df['Week'] = df['Date'].dt.isocalendar().week #Criação do atributo Week
    df['DayOfWeek'] = df['Date'].dt.dayofweek #Criação do atributo Day of Week
    df['YearMonth'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m')) #Criação do atributo Year/Month
    df['Data'] = df['Date'].dt.strftime('%Y/%m/%d') #Criação do atributo Year/Month/Day
    


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

    df['NameMonths'] = df['Month'].map(months_map) #Criação do atributo Months Names

    df['NameDayOfWeek'] = df['DayOfWeek'].map(dayweek_map) #Criação do atributo Days of Weeks Name

    return df


# Função que realiza o agrupamento dos dados, por: Somatório, Média ou Mediana.
def agrupaDados(list_df, columns, tipo_agrupamento):
    list_res = []

    tipo_agrupamento = 'mean' if tipo_agrupamento == 'Média' else 'sum' if tipo_agrupamento == 'Somatório' else 'median' 

    for df in list_df:
        aux_df = df.groupby(columns, as_index=False).agg(tipo_agrupamento)
        if columns[0] == 'YearMonth':
            aux_df['Year Month'] = aux_df['YearMonth'].dt.strftime('%Y/%m')
        list_res.append(aux_df)




    return list_res


# Função responsável por criar um dataframe gerando datas de acordo com o agrupamento selecionado, por Dia, Mês, Week e Ano. 
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

# Converte um valor inteiro para Data
def timeStampToDate(value):
    try:
        date = datetime.datetime.fromtimestamp(value)
        resultado = f'{date.year}/{date.month}/{date.day} {date.hour}:{date.minute}'
        return resultado

    except:
        return '-'
