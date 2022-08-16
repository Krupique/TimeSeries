import time
# Visualização dos dados
import matplotlib.pyplot as plt
import matplotlib as m
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff


import streamlit as st
from datetime import date
from PIL import Image
import pandas as pd
import numpy as np

from include.coleta import coletaDados, agrupaDados, geraDatas
from include.graphs import exibirGrafico, exibirCanddleStick, adicionarTrace, exibirGraficoSustentabilidade
from include.calculos import calculaRentabilidade, decomporSerie, calculaEstacionaridade, calculaMediaMovel, calculaDesvioPadrao, currencyFormatting
from include.modelo import Preditor


################################################# Declaração de variáveis ##################################################
df = []
list_tickers = []

################################################# Funções e métodos Python ##################################################
ref_file = open("utils/lista_siglas.txt","r")
for row in ref_file:
    row = row.upper().replace('\n', '')
    list_tickers.append(row)

################################################# Funções e métodos Streamlit ##################################################
st.set_page_config(layout='wide')

def sidebar_features():
    image = Image.open('assets/img.jpeg')
    st.sidebar.image(image, use_column_width=True)
    st.sidebar.header('Realizado por : Henrique Krupck')
    # Contatos
    st.sidebar.markdown("Contatos :")
    st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/henrique-krupck/)")
    st.sidebar.markdown("- [Github](https://github.com/krupique)")

def validar_alteracoes(list_selected, input_dt_ini, input_dt_fim, option, tipo_agrupamento):
    resultado = True

    if 'validar_alteracoes' not in st.session_state:
        st.session_state['validar_alteracoes'] = True

    else:
        if not (st.session_state['list_selected'] == list_selected and st.session_state['input_dt_ini'] == input_dt_ini and st.session_state['input_dt_fim'] == input_dt_fim and  st.session_state['option'] == option and st.session_state['tipo_agrupamento'] == tipo_agrupamento):
            resultado = False

    st.session_state['list_selected'] = list_selected
    st.session_state['input_dt_ini'] = input_dt_ini
    st.session_state['input_dt_fim'] = input_dt_fim
    st.session_state['option'] = option
    st.session_state['tipo_agrupamento'] = tipo_agrupamento

    return resultado



def main_page():

    list_selected = st.multiselect( 'Selecione a empresa', list_tickers)
    c1, c2, c3, c4 = st.columns(4)

    input_dt_ini = c1.date_input("Data Inicial")
    input_dt_fim = c2.date_input("Data Final")
    option = c3.selectbox( 'Selecione o agrupamento por data ', ('Dia', 'Semana', 'Mês', 'Ano')) 
    tipo_agrupamento = c4.selectbox( 'Selecione o método de agrupamento ', ('Somatório', 'Média', 'Mediana')) 


    flag_coleta = False
    if st.button('Coletar Dados'):
        df_info, list_dfs, list_dfs_quartfinancials, list_dfs_sustainability, list_dfs_news = coletaDados(list_selected, interval='1d', start=input_dt_ini.strftime("%Y-%m-%d"), end=input_dt_fim.strftime("%Y-%m-%d"))
        flag_coleta = True

        #if 'flag' not in st.session_state:
        st.session_state['flag'] = 'OK'

        st.session_state['df_info'] = df_info
        st.session_state['list_dfs'] = list_dfs
        st.session_state['list_dfs_quartfinancials'] = list_dfs_quartfinancials
        st.session_state['list_dfs_sustainability'] = list_dfs_sustainability
        st.session_state['list_dfs_news'] = list_dfs_news
    else:
        if validar_alteracoes(list_selected, input_dt_ini, input_dt_fim, option, tipo_agrupamento):
            if 'flag' in st.session_state:
                flag_coleta = True
                df_info = st.session_state['df_info']
                list_dfs = st.session_state['list_dfs']
                list_dfs_quartfinancials = st.session_state['list_dfs_quartfinancials']
                list_dfs_sustainability = st.session_state['list_dfs_sustainability']
                list_dfs_news = st.session_state['list_dfs_news']

        else:
            flag_coleta = False
            

    tab1, tab2, tab3 = st.tabs(['Visão Geral dos Dados', 'Análise Estatística', 'Análise Preditiva'])

    if len(list_selected) > 0 and flag_coleta:

        if input_dt_ini < input_dt_fim and input_dt_ini < date.today():

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

                                c1, c2, c3 = st.columns(3)

                                financialCurrency = df_aux_info['financialCurrency'].values[0]
                                currentPrice = df_aux_info['currentPrice'].values[0]
                                earningsGrowth = df_aux_info['earningsGrowth'].values[0]
                                recommendationKey = df_aux_info['recommendationKey'].values[0]
                                recommendationMean = df_aux_info['recommendationMean'].values[0]
                                numberOfAnalystOpinions = df_aux_info['numberOfAnalystOpinions'].values[0]
                                targetMeanPrice = df_aux_info['targetMeanPrice'].values[0]
                                market = df_aux_info['market'].values[0]


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

                                df_trimestre['Gross Profit Transformed'] = df_trimestre['Gross Profit'].apply(currencyFormatting)
                                df_trimestre['Net Income Transformed'] = df_trimestre['Net Income'].apply(currencyFormatting)
                                df_trimestre['Total Revenue Transformed'] = df_trimestre['Total Revenue'].apply(currencyFormatting)

                                c1, c2, c3, c4 = st.columns(4)



                                trimestres = [] 
                                for data in df_trimestre.index:
                                    trimestres.append(f'{data.year}-{data.month}')

                                lucro_bruto = df_trimestre.iloc[0]['Gross Profit Transformed']
                                resultado_liquido = df_trimestre.iloc[0]['Net Income Transformed']
                                rendimento_total = df_trimestre.iloc[0]['Total Revenue Transformed']
                                #c1.markdown(f"<p style='text-align: center;'>{trimestres[0]}</p>", unsafe_allow_html=True)
                                c1.markdown(f'{trimestres[0]}')
                                c1.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                c1.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                c1.markdown(f'Rendimento Total: **{rendimento_total}**')


                                lucro_bruto = df_trimestre.iloc[1]['Gross Profit Transformed']
                                resultado_liquido = df_trimestre.iloc[1]['Net Income Transformed']
                                rendimento_total = df_trimestre.iloc[1]['Total Revenue Transformed']
                                #c2.markdown(f"<p style='text-align: center;'>{trimestres[1]}</p>", unsafe_allow_html=True)
                                c2.markdown(f'{trimestres[1]}')
                                c2.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                c2.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                c2.markdown(f'Rendimento Total: **{rendimento_total}**')
                                

                                lucro_bruto = df_trimestre.iloc[2]['Gross Profit Transformed']
                                resultado_liquido = df_trimestre.iloc[2]['Net Income Transformed']
                                rendimento_total = df_trimestre.iloc[2]['Total Revenue Transformed']
                                #c3.markdown(f"<p style='text-align: center;'>{trimestres[2]}</p>", unsafe_allow_html=True)
                                c3.markdown(f'{trimestres[2]}')
                                c3.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                c3.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                c3.markdown(f'Rendimento Total: **{rendimento_total}**')
                                

                                lucro_bruto = df_trimestre.iloc[3]['Gross Profit Transformed']
                                resultado_liquido = df_trimestre.iloc[3]['Net Income Transformed']
                                rendimento_total = df_trimestre.iloc[3]['Total Revenue Transformed']
                                #c4.markdown(f"<p style='text-align: center;'>{trimestres[3]}</p>", unsafe_allow_html=True)
                                c4.markdown(f'{trimestres[3]}')
                                c4.markdown(f'Lucro Bruto: **{lucro_bruto}**')
                                c4.markdown(f'Resultado Líquido: **{resultado_liquido}**')
                                c4.markdown(f'Rendimento Total: **{rendimento_total}**')



                                st.markdown("""---""")

                                st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")
                                st.write(list_df_agrupados[i][display_columns])

                                figCandlestick = exibirCanddleStick(list_df_agrupados[i], column_x, list_selected[i], title='Gráfico Candlestick da ação', width=1000, height=500, xlabel='Período', ylabel='Valores')
                                
                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 7)
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 7 dias', color = '#FF0')
                                
                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 15)
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 15 dias', color = '#323ca8')

                                df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 30)
                                figCandlestick = adicionarTrace(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 30 dias', color = '#a8329b')
                                
                                st.write(figCandlestick)

                            with tab02:
                                
                                st.markdown('### Resumo da empresa')
                                c1, c2 = st.columns(2)

                                

                                c1.markdown('**Informações Básicas**')

                                shortName = df_aux_info['shortName'].values[0]
                                c1.markdown(f'Nome abreviado: **{shortName}**')

                                longName = df_aux_info['longName'].values[0]
                                c1.markdown(f'Nome completo: **{longName}**')

                                sector = df_aux_info['sector'].values[0]
                                c1.markdown(f'Setor de atuação: **{sector}**')

                                industry = df_aux_info['industry'].values[0]
                                c1.markdown(f'Tipo de serviço: **{industry}**')

                                employees = df_aux_info['fullTimeEmployees'].values[0]
                                c1.markdown(f'Quantidade de colaboradores: **{employees}**')

								
                                ###########################################################
                                c2.markdown('**Informações de Endereço e Contato**')
                                
                                city = df_aux_info['city'].values[0]
                                c2.markdown(f'Tipo de serviço: **{industry}**')
                                
                                country = df_aux_info['country'].values[0]
                                c2.markdown(f'Pais da sede: **{country}**')


                                phone = df_aux_info['phone'].values[0]
                                c2.markdown(f'Telefone: **{phone}**')

                                website = df_aux_info['website'].values[0]
                                c2.markdown(f'Website: **{website}**')

                                logo_url = df_aux_info['logo_url'].values[0]
                                c2.write('Logo da empresa')
                                c2.image(logo_url)


                                st.markdown("""---""")

                                st.markdown('**Sobre a Empresa**')
                                longText = df_aux_info['longBusinessSummary'].values[0]
                                st.write(longText)

                                st.markdown("""---""")

                                df_sustainability = list_dfs_sustainability[i]
                                mes = df_sustainability.columns.name

                                st.markdown(f'**Avaliação de Sustentabilidade da organização no período {mes}**')

                                x_values = df_sustainability.columns
                                y_values = df_sustainability.values[0]

                                c1, c2, c3, c4 = st.columns(4)

                                c1.metric('Score Total', y_values[3])
                                c2.metric('Score Social', y_values[0])
                                c3.metric('Score Governamental', y_values[1])
                                c4.metric('Score Ambiental', y_values[2])

                                #fig = exibirGraficoSustentabilidade(x_values, y_values, 700, 300)
                                #st.write(fig)




                            with tab03:

                                st.markdown('### Últimas Notícias relacionadas ao Ativo')

                                df_news = list_dfs_news[i]

                                for row in df_news.iterrows():
                                    st.markdown(f'<a target="_blank" href="{row[1].link}">{row[1].title}</a>', unsafe_allow_html=True)
                                    st.caption(f'{row[1].publisher} {row[1].date}')



                    st.markdown("""---""")

                    st.markdown('#### Comparação dos ativos')

                    figureTimeSerie = exibirGrafico(list_df_agrupados, list_selected, type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação]', xlabel='Período', ylabel='Valor', width=700)
                    df_rentabilidade = calculaRentabilidade(list_df_agrupados, list_selected)
                    

                    
                    c1, c2 = st.columns([0.3, 0.7])

                    c1.write('Rentabilidade das ações')
                    c1.write(df_rentabilidade)
                    c2.write(figureTimeSerie)



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

                            st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")

                            figureBarPlot = exibirGrafico([list_dfs[i]], type='box', list_tickers = list_selected, x='Year', y='Close', title='Boxplot por ano para análise interquartil', xlabel='Período', ylabel='Valor', width=300, height=400)
                            figureHistogram = exibirGrafico([list_dfs[i]], type='histogram',list_tickers = list_selected , x='Close', y='Close', title='Histograma com valores de Fechamento', xlabel='Valores', ylabel='Quantidade', width=300, height=400)
                            
                            df_adfuller = calculaEstacionaridade(list_dfs[i], 'Close')
                            
                            if optionDecompose == 'Aditiva':
                                list_df_decomposition = decomporSerie(list_dfs[i], 'aditive')

                            else: #Multiplicativa
                                list_df_decomposition = decomporSerie(list_dfs[i], 'multiplicative')

                            
                            

                            c1, c2, c3 = st.columns(3)

                            c1.write('Teste Dickey-Fuller aumentado')
                            c1.write(df_adfuller)

                            valor_p = df_adfuller.loc[df_adfuller.index == 'Valor-p', 'Resultados'].values[0]
                            if valor_p > 0.05:
                                c1.write('O valor-p é maior que 0.05 e, portanto, essa série provavelmente não é estacionária.')
                            else: 
                                c1.write('O valor-p é maior que 0.05 e, portanto, essa série provavelmente é estacionária.')

                            c2.write(figureBarPlot)
                            c3.write(figureHistogram)

                            st.markdown("""---""")

                            figureDecompose1 = exibirGrafico([list_df_decomposition[0]], list_df_decomposition[0].name , type='line', x='Date', y='Value', title=f'Elemento {list_df_decomposition[0].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)
                            figureDecompose2 = exibirGrafico([list_df_decomposition[1]], list_df_decomposition[1].name , type='line', x='Date', y='Value', title=f'Elemento {list_df_decomposition[1].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)
                            figureDecompose3 = exibirGrafico([list_df_decomposition[2]], list_df_decomposition[2].name , type='line', x='Date', y='Value', title=f'Elemento {list_df_decomposition[2].name} da série decomposta', xlabel='Período', ylabel='Valor', height=300)

                            figureTimeSerie = exibirGrafico([list_df_agrupados[i]], list_selected, type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação e Desvio Padrão]', xlabel='Período', ylabel='Valor')
                            df_desvio = calculaDesvioPadrao(list_df_agrupados[i], days=7)
                            figureTimeSerie = adicionarTrace(figureTimeSerie, df_desvio, x = column_x, y='DesvioPadrao', name='Desvio Padrão', color='#FF0')


                            st.write(figureDecompose1)
                            st.write(figureDecompose2)
                            st.write(figureDecompose3)

                            st.markdown("""---""")
                            st.write(figureTimeSerie)

            with tab3:
                st.header('Análise Preditiva')
                if len(list_dfs) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    c1, c2 = st.columns(2)
                    period = c1.slider('Escolha a quantidade de períodos para a previsão.', 0, 120, 7)
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

    # transformation
    sidebar_features()

    main_page()