import time

import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff

import streamlit as st
from datetime import date
from PIL import Image
import pandas as pd
import numpy as np

from include.coleta import coletaDados, agrupaDados, geraDatas
from include.graphs import exibirGrafico, exibirCanddleStick, adicionarTrace
from include.calculos import calculaRentabilidade, decomporSerie, calculaEstacionaridade, calculaMediaMovel, calculaDesvioPadrao, currencyFormatting
from include.modelo import Preditor

df = []
list_tickers = []

# Carrega arquivo de siglas(tickers) disponíveis
# O arquivo lista_siglas é customizável, portanto, caso deseje incluir mais organizações, basta navegar até este arquivo e adicionar suas próprias ações.
# Vale lembrar que para um ticker personalizado é necessário que este ticker esteja disponível no Yahoo Finance e que esteja funcionando de acordo com o padrão da API.
ref_file = open("utils/lista_siglas.txt","r")
for row in ref_file:
    row = row.upper().replace('\n', '')
    list_tickers.append(row)

ref_file.close() 

# Configurações básicas da página
st.set_page_config(
    page_title="Preditor de Ações",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Krupique/TimeSeries/tree/main/03_PreditorAcoes',
        'Report a bug': "https://www.linkedin.com/in/henrique-krupck/",
        'About': "This project is maintained by Henrique Krupck. All project documentation, details and description of each technique used are in the [official repository on github](https://github.com/Krupique/TimeSeries/tree/main/03_PreditorAcoes)."
    }
)

# @Obsolete 
# Adiciona seu próprio ticker ao cache 
def add_ticker_cache(own_ticker):
    if 'list_own_tickers' not in st.session_state:
        st.session_state['list_own_tickers'] = [own_ticker]

    else:
        st.session_state['list_own_tickers'].append(own_ticker)

    list_tickers.extend(st.session_state['list_own_tickers'])

# Barra lateral com o logo, informações do criador do site, links direcionando ao repositório
def sidebar_features():

    st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Stock Analytics</h1>", unsafe_allow_html=True)

    image = Image.open('assets/logo2.jpg')
    st.sidebar.image(image, use_column_width=True)
    
    # Sobre
    st.sidebar.subheader("Sobre")
    st.sidebar.markdown('<div style="text-align: justify; padding:5px; color:#1e6777; border-radius:3px; background-color:#dbe6f4; border: 1px solid #c8dcf3;">Este projeto foi realizado por Henrique Krupck. Toda a documentação do projeto, detalhes e descrição de cada técnica utilizada estão no <a target="_blank" href="https://github.com/Krupique/TimeSeries/tree/main/03_PreditorAcoes">repositório oficial no github</a>.</div>', unsafe_allow_html=True)
    
    # Contatos
    st.sidebar.subheader("Contatos")
    st.sidebar.markdown('<div style="text-align: justify; padding:5px; color:#1e6777; border-radius:3px; background-color:#dbe6f4; border: 1px solid #c8dcf3;">Você pode me encontrar em:<ul><li><a target="_blank" href="https://www.linkedin.com/in/henrique-krupck/">Linkedin</a></li><li><a target="_blank" href="https://github.com/krupique">Github</a></li><li><a target="_blank" href="mailto:krupck@outlook.com">Email</a></li></ul></div>', unsafe_allow_html=True)


# Essa função valida se houve alterações por parte do usuário nos campos que foram passados por parâmetro
def validar_alteracoes(list_selected, input_dt_ini, input_dt_fim, option, tipo_agrupamento):
    resultado = True

    # Se a variável booleana não estiver no cache da sessão, então adiciona ao cache
    if 'validar_alteracoes' not in st.session_state:
        st.session_state['validar_alteracoes'] = True

    else:
        #Se não houve alterações por parte do usuário, então o resultado é Falso
        if not (st.session_state['list_selected'] == list_selected and st.session_state['input_dt_ini'] == input_dt_ini and st.session_state['input_dt_fim'] == input_dt_fim):
            resultado = False

    #Adiciona os dados ao cache
    st.session_state['list_selected'] = list_selected
    st.session_state['input_dt_ini'] = input_dt_ini
    st.session_state['input_dt_fim'] = input_dt_fim

    return resultado


# Página principal, aqui que tudo acontece
def main_page():

    #Inputs
    list_selected = st.multiselect( 'Selecione a empresa', list_tickers)
    c1, c2, c3, c4 = st.columns(4)

    input_dt_ini = c1.date_input("Data Inicial")
    input_dt_fim = c2.date_input("Data Final")
    option = c3.selectbox( 'Selecione o agrupamento por data ', ('Dia', 'Semana', 'Mês', 'Ano')) 
    tipo_agrupamento = c4.selectbox( 'Selecione o método de agrupamento ', ('Somatório', 'Média', 'Mediana')) 


    flag_coleta = False
    #Evento do clique coletar dados
    if st.button('Coletar Dados'): #Se clicou no botão coletar dados, então adicione todos os dados obtidos ao cache.
        df_info, list_dfs, list_dfs_quartfinancials, list_dfs_sustainability, list_dfs_news = coletaDados(list_selected, interval='1d', start=input_dt_ini.strftime("%Y-%m-%d"), end=input_dt_fim.strftime("%Y-%m-%d"))
        flag_coleta = True
        
        st.session_state['flag'] = 'OK'

        st.session_state['df_info'] = df_info
        st.session_state['list_dfs'] = list_dfs
        st.session_state['list_dfs_quartfinancials'] = list_dfs_quartfinancials
        st.session_state['list_dfs_sustainability'] = list_dfs_sustainability
        st.session_state['list_dfs_news'] = list_dfs_news
    else: #Senão, valida as alterações
        if validar_alteracoes(list_selected, input_dt_ini, input_dt_fim, option, tipo_agrupamento):
            #Se validou as informações, então adiciona os dados coletados ao cache
            if 'flag' in st.session_state:
                flag_coleta = True
                df_info = st.session_state['df_info']
                list_dfs = st.session_state['list_dfs']
                list_dfs_quartfinancials = st.session_state['list_dfs_quartfinancials']
                list_dfs_sustainability = st.session_state['list_dfs_sustainability']
                list_dfs_news = st.session_state['list_dfs_news']

        else:
            flag_coleta = False
            

    #Criamos três abas, uma para cada tipo de análise.
    tab1, tab2, tab3 = st.tabs(['Visão Geral dos Dados', 'Análise Estatística', 'Análise Preditiva'])

    # Se o usuário selecionou um ticker e os dados foram coletados
    if len(list_selected) > 0 and flag_coleta:

        #Se a data inicial for menor que a data final e a data inicial for menor do que hoje
        if input_dt_ini < input_dt_fim and input_dt_ini < date.today():

            # Qual foi a opção de agrupamento, dia, semana, mês ou ano?
            # Verifica e agrupa os dados de acordo com a opção escolhida
            if option == 'Dia':
                column_x = 'Date'
                list_df_agrupados = list_dfs
                display_columns = ['Data', 'Open', 'High', 'Low', 'Close', 'Volume', 'Week', 'NameDayOfWeek']

            elif option == 'Semana':
                column_x = 'Week'
                list_df_agrupados = agrupaDados(list_dfs, [column_x], tipo_agrupamento)
                display_columns = ['Week', 'Open', 'High', 'Low', 'Close', 'Volume']

            elif option == 'Mês':
                column_x = 'YearMonth'
                list_df_agrupados = agrupaDados(list_dfs, [column_x], tipo_agrupamento)
                display_columns = ['Year Month', 'Open', 'High', 'Low', 'Close', 'Volume']
            
            elif option == 'Ano':
                column_x = 'Year'
                list_df_agrupados = agrupaDados(list_dfs, [column_x], tipo_agrupamento)
                display_columns = ['Year', 'Open', 'High', 'Low', 'Close', 'Volume']


            #Tudo referente a aba de visão geral dos dados
            with tab1:
                st.header('Visão Geral dos Dados')

                if len(list_dfs) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    tabs_empresas = st.tabs(list_selected)


                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:

                            tab01, tab02, tab03 = st.tabs(['Dados de Ações', 'Resumo da empresa', 'Notícias'])
                            
                            df_aux_info = df_info.loc[df_info.index == list_selected[i]]

                            with tab01:

                                st.markdown('### Informações do Ativo')
                                
                                if len(df_aux_info) == 0:
                                    st.markdown("""**Não foi possível as informações sobre os detalhes da empresa.**""")
                                else:
                                    financialCurrency = df_aux_info['financialCurrency'].values[0]
                                    currentPrice = df_aux_info['currentPrice'].values[0]
                                    earningsGrowth = df_aux_info['earningsGrowth'].values[0]
                                    recommendationKey = df_aux_info['recommendationKey'].values[0]
                                    recommendationMean = df_aux_info['recommendationMean'].values[0]
                                    numberOfAnalystOpinions = df_aux_info['numberOfAnalystOpinions'].values[0]
                                    targetMeanPrice = df_aux_info['targetMeanPrice'].values[0]
                                    market = df_aux_info['market'].values[0]

                                    c1, c2, c3 = st.columns(3)
                                    c1.metric(label="Moeda Padrão", value=financialCurrency, delta=market)
                                    c2.metric(label="Valor Atual (Ganhos p/cresc)", value=currentPrice, delta=earningsGrowth)
                                    c3.metric(label="Avaliação de Recomendação", value=recommendationKey, delta=float(recommendationMean), delta_color="off")
                                    
                                    st.write("")

                                    c1, c2 = st.columns(2)
                                    c1.markdown(f'Recomendação de Especialistas: **{recommendationKey}**')
                                    c1.markdown(f'Média de Recomendação: **{recommendationMean}**')
                                    c1.markdown(f'Opinião de [**{numberOfAnalystOpinions}**] especialistas')
                                    c2.markdown(f'Valor atual do ativo: **{currentPrice}**')
                                    c2.markdown(f'Preço médio do Alvo: **{targetMeanPrice}**')
                                    c2.markdown(f'Ganhos por Crescimento: **{earningsGrowth}**')

                                st.markdown("""---""")
                                st.markdown("**Resultados dos últimos trimestres**")
                                
                                df_trimestre = list_dfs_quartfinancials[i]
                                if len(df_trimestre) == 0:
                                    st.markdown("""**Não foi possível obter as informações sobre os detalhes da empresa.**""")
                                else:
                                    df_trimestre['Gross Profit Transformed'] = df_trimestre['Gross Profit'].apply(currencyFormatting)
                                    df_trimestre['Net Income Transformed'] = df_trimestre['Net Income'].apply(currencyFormatting)
                                    df_trimestre['Total Revenue Transformed'] = df_trimestre['Total Revenue'].apply(currencyFormatting)

                                    trimestres = [] 
                                    for data in df_trimestre.index:
                                        trimestres.append(f'{data.year}-{data.month}')

                                    c1, c2, c3, c4 = st.columns(4)

                                    lucro_bruto = df_trimestre.iloc[0]['Gross Profit Transformed']
                                    resultado_liquido = df_trimestre.iloc[0]['Net Income Transformed']
                                    rendimento_total = df_trimestre.iloc[0]['Total Revenue Transformed']
                                    c1.markdown(f'{trimestres[0]}')
                                    c1.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                    c1.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                    c1.markdown(f'Rendimento Total: **{rendimento_total}**')


                                    lucro_bruto = df_trimestre.iloc[1]['Gross Profit Transformed']
                                    resultado_liquido = df_trimestre.iloc[1]['Net Income Transformed']
                                    rendimento_total = df_trimestre.iloc[1]['Total Revenue Transformed']
                                    c2.markdown(f'{trimestres[1]}')
                                    c2.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                    c2.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                    c2.markdown(f'Rendimento Total: **{rendimento_total}**')
                                    

                                    lucro_bruto = df_trimestre.iloc[2]['Gross Profit Transformed']
                                    resultado_liquido = df_trimestre.iloc[2]['Net Income Transformed']
                                    rendimento_total = df_trimestre.iloc[2]['Total Revenue Transformed']
                                    c3.markdown(f'{trimestres[2]}')
                                    c3.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                    c3.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                    c3.markdown(f'Rendimento Total: **{rendimento_total}**')
                                    

                                    lucro_bruto = df_trimestre.iloc[3]['Gross Profit Transformed']
                                    resultado_liquido = df_trimestre.iloc[3]['Net Income Transformed']
                                    rendimento_total = df_trimestre.iloc[3]['Total Revenue Transformed']
                                    c4.markdown(f'{trimestres[3]}')
                                    c4.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                    c4.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                    c4.markdown(f'Rendimento Total: **{rendimento_total}**')

                                st.markdown("""---""")


                                
                                lista_dias = [7, 15, 30]
                                texto = 'Dias'
                                if column_x == 'Week':
                                    lista_dias = [5, 10, 20]
                                    texto = 'Semanas'
                                
                                elif column_x == 'YearMonth':
                                    lista_dias = [3, 6, 12]
                                    texto = 'Meses'

                                elif column_x == 'Year':
                                    lista_dias = [2, 3, 5]
                                    texto = 'Anos'

                                st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")
                                st.write(list_df_agrupados[i][display_columns])
                                figCandlestick = exibirCanddleStick(list_df_agrupados[i], column_x, list_selected[i], title='Gráfico Candlestick da ação', width=1000, height=500, xlabel='Período', ylabel='Valores')
                                

                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = lista_dias[0])
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= f'Média móvel {lista_dias[0]} {texto}', color = '#FF0')
                                
                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = lista_dias[1])
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= f'Média móvel {lista_dias[1]} {texto}', color = '#323ca8')

                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = lista_dias[2])
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= f'Média móvel {lista_dias[2]} {texto}', color = '#a8329b')
                                
                                st.write(figCandlestick)


                            with tab02:
                                
                                st.markdown('### Resumo da empresa')

                                if len(df_aux_info) == 0:
                                    st.markdown("""**Não foi possível as informações sobre os detalhes da empresa.**""")
                                else:
                                    shortName = df_aux_info['shortName'].values[0]
                                    longName = df_aux_info['longName'].values[0]
                                    sector = df_aux_info['sector'].values[0]
                                    industry = df_aux_info['industry'].values[0]
                                    employees = df_aux_info['fullTimeEmployees'].values[0]
                                    city = df_aux_info['city'].values[0]
                                    country = df_aux_info['country'].values[0]
                                    phone = df_aux_info['phone'].values[0]
                                    website = df_aux_info['website'].values[0]
                                    logo_url = df_aux_info['logo_url'].values[0]
                                    longText = df_aux_info['longBusinessSummary'].values[0]
                                    

                                    c1, c2 = st.columns(2)
                                    c1.markdown('**Informações Básicas**')
                                    c1.markdown(f'Nome abreviado: **{shortName}**')
                                    c1.markdown(f'Nome completo: **{longName}**')
                                    c1.markdown(f'Setor de atuação: **{sector}**')
                                    c1.markdown(f'Tipo de serviço: **{industry}**')
                                    c1.markdown(f'Quantidade de colaboradores: **{employees}**')
                                    c2.markdown('**Informações de Endereço e Contato**')
                                    c2.markdown(f'Tipo de serviço: **{industry}**')
                                    c2.markdown(f'Pais da sede: **{country}**')
                                    c2.markdown(f'Telefone: **{phone}**')
                                    c2.markdown(f'Website: **{website}**')
                                    c2.write('Logo da empresa')
                                    c2.image(logo_url)

                                    st.markdown("""---""")
                                    st.markdown('**Sobre a Empresa**')
                                    st.write(longText)

                                st.markdown("""---""")

                                df_sustainability = list_dfs_sustainability[i]
                                if len(df_sustainability) == 0:
                                    st.markdown("""**Não foi possível buscar informações sobre as pontuações de sustentabilidade da organização**""")
                                
                                else:
                                    mes = df_sustainability.columns.name
                                    x_values = df_sustainability.columns
                                    y_values = df_sustainability.values[0]


                                    st.markdown(f'**Avaliação de Sustentabilidade da organização no período {mes}**')
                                    c1, c2, c3, c4 = st.columns(4)
                                    c1.metric('Score Total', y_values[3])
                                    c2.metric('Score Social', y_values[0])
                                    c3.metric('Score Governamental', y_values[1])
                                    c4.metric('Score Ambiental', y_values[2])


                            with tab03:

                                st.markdown('### Últimas Notícias relacionadas ao Ativo')
                                df_news = list_dfs_news[i]

                                if len(df_news) == 0:
                                    st.markdown("""**Não foi possível buscar as últimas notícias relacionadas ao ativo.**""")
                                else:
                                    for row in df_news.iterrows():
                                        st.markdown(f'<a target="_blank" href="{row[1].link}">{row[1].title}</a>', unsafe_allow_html=True)
                                        st.caption(f'{row[1].publisher} {row[1].date}')
                                        st.write('\n')



                    st.markdown("""---""")

                    st.markdown('#### Comparação dos ativos')

                    figureTimeSerie = exibirGrafico(list_df_agrupados, list_selected, type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação]', xlabel='Período', ylabel='Valor', width=700)
                    df_rentabilidade = calculaRentabilidade(list_df_agrupados, list_selected)
                    

                    
                    c1, c2 = st.columns([0.3, 0.7])

                    c1.write('Rentabilidade das ações')
                    c1.write(df_rentabilidade)
                    c2.write(figureTimeSerie)


            #Tudo referente a aba de Análise Estatística
            with tab2:
                st.header('Análise Estatística')
                if len(list_dfs) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    optionDecompose = st.radio(
                            "Escolha o tipo de decomposição: ",
                            ('Aditiva', 'Multiplicativa'))


                    tabs_empresas = st.tabs(list_selected)
                    

                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:

                            if len(list_df_agrupados[i]) > 3:

                                st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")

                                figureBarPlot = exibirGrafico([list_dfs[i]], type='box', list_tickers = list_selected, x='Year', y='Close', title='Boxplot por ano para análise interquartil', xlabel='Período', ylabel='Valor', width=300, height=400)
                                figureHistogram = exibirGrafico([list_df_agrupados[i]], type='histogram',list_tickers = list_selected , x='Close', y='Close', title='Histograma com valores de Fechamento', xlabel='Valores', ylabel='Quantidade', width=300, height=400)
                                
                                df_adfuller = calculaEstacionaridade(list_df_agrupados[i], 'Close')
                                

                                c1, c2, c3 = st.columns(3)

                                c1.write('Teste Dickey-Fuller aumentado')
                                c1.write(df_adfuller)

                                valor_p = df_adfuller.loc[df_adfuller.index == 'Valor-p', 'Resultados'].values[0]
                                if valor_p > 0.05:
                                    c1.write('O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula. Essa série provavelmente não é estacionária.')
                                else: 
                                    c1.write('O valor-p é maior que 0.05 e, logo, temos fortes evidências para rejeitar a hipótese nula. Essa série provavelmente é estacionária.')

                                c2.write(figureBarPlot)
                                c3.write(figureHistogram)

                                st.markdown("""---""")

                                if len(list_df_agrupados[i]) > 100:
                                    if optionDecompose == 'Aditiva':
                                        list_df_decomposition = decomporSerie(list_df_agrupados[i], 'aditive', column_x)

                                    else: #Multiplicativa
                                        list_df_decomposition = decomporSerie(list_df_agrupados[i], 'multiplicative', column_x)

                                    figureDecompose1 = exibirGrafico([list_df_decomposition[0]], list_df_decomposition[0].name , type='line', x=column_x, y='Value', title=f'Elemento {list_df_decomposition[0].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)
                                    figureDecompose2 = exibirGrafico([list_df_decomposition[1]], list_df_decomposition[1].name , type='line', x=column_x, y='Value', title=f'Elemento {list_df_decomposition[1].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)
                                    figureDecompose3 = exibirGrafico([list_df_decomposition[2]], list_df_decomposition[2].name , type='line', x=column_x, y='Value', title=f'Elemento {list_df_decomposition[2].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)

                                    st.write(figureDecompose1)
                                    st.write(figureDecompose2)
                                    st.write(figureDecompose3)
                                else:
                                    st.write('Para decompor a Série é necessário um valor mínimo de 100 observações.')


                                figureTimeSerie = exibirGrafico([list_df_agrupados[i]], list_selected, type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação e Desvio Padrão]', xlabel='Período', ylabel='Valor')
                                df_desvio = calculaDesvioPadrao(list_df_agrupados[i], days=7)
                                figureTimeSerie = adicionarTrace(figureTimeSerie, df_desvio, x = column_x, y='DesvioPadrao', name='Desvio Padrão', color='#FF0')

                                st.markdown("""---""")
                                st.write(figureTimeSerie)

                            else:
                                st.write('É necessário uma quantidade de períodos maior do que três [3] para verificar as medidas estatísticas.')

            #Tudo referente a aba de Análise Preditiva
            with tab3:
                st.header('Análise Preditiva')
                if len(list_dfs) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    c1, c2 = st.columns(2)
                    period = c1.slider('Escolha a quantidade de períodos para a previsão.', 0, 120, 15)
                    periodiocity = c2.number_input('Nível de Periodicidade. Valor recomendado: 15 períodos', value = 15, min_value = 5, max_value = 35)
                    

                    c1.write('NOTA: Quanto mais distante o período que se quer prever, maior é o grau de incerteza.')
                    c2.write('NOTA: Valores baixos são mais velozes em performance, valores altos são mais precisos, porém mais custosos.')
                    
                    
                    clicked = st.button("Treinar o modelo")

                    tabs_empresas = st.tabs(list_selected)


                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:

                            if clicked:
                                
                                # Info para o usuário

                                if column_x == 'Week':
                                    st.write('Não é possível realizar previsões para este tipo de agrupamento. Por favor, tente utilizar Dias [Date], Mês [YearMonth] ou Ano [Year]')

                                else:
                                    preditor = Preditor(list_df_agrupados[i], 'Close', periodiocity)
                                    previsoes = preditor.predict(period = period)

                                    dataInicial = list_df_agrupados[i].iloc[-1][column_x]
                                    df_previsoes = geraDatas(previsoes, dataInicial, column_x)

                                    figureTimeSerie = exibirGrafico([list_df_agrupados[i]], ['Valores Reais'], type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação e Previsões realizadas]', xlabel='Período', ylabel='Valor', width=700)
                                    figureTimeSerie = adicionarTrace(fig = figureTimeSerie, df = df_previsoes, x = column_x, y = 'Valores Previstos', name='Valores Previstos', color='#FF0')

                                    c1, c2 = st.columns([0.3, 0.7])
                                    c1.write('Tabela com valores previstos pelo modelo')
                                    c1.write(df_previsoes[['Data', 'Valores Previstos']])
                                    c2.write(figureTimeSerie)

 

        else:
            st.write('A data inicial deve ser menor que a data final e a data inicial deve ser menor que o dia atual')

        



###############################################################################################################
if __name__ == '__main__':

    sidebar_features()

    main_page()