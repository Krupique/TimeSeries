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

from include.coleta import coletaDados, agrupaDados
from include.graphs import exibirGrafico, exibirCanddleStick, adicionarMediaMovel
from include.calculos import calculaRentabilidade, decompor_serie, calculaEstacionaridade, calculaMediaMovel


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


def main_page():

    list_selected = st.multiselect( 'Selecione a empresa', list_tickers)
    c1, c2 = st.columns(2)

    input_dt_ini = c1.date_input("Data Inicial")
    input_dt_fim = c2.date_input("Data Final")

    option = st.selectbox( 'Exibir informações agrupadas por: ', ('Dia', 'Semana', 'Mês', 'Ano')) 

    tab1, tab2, tab3, tab4 = st.tabs(['Visão Geral dos Dados', 'Análise Estatística', 'Análise Descritiva', 'Análise Preditiva'])

    if len(list_selected) > 0:

        

        if input_dt_ini < input_dt_fim and input_dt_ini < date.today():

            #Coletando os dados
            list_df = coletaDados(list_selected, interval='1d', start=input_dt_ini.strftime("%Y-%m-%d"), end=input_dt_fim.strftime("%Y-%m-%d"))
            
            if option == 'Dia':
                column_x = 'Date'
                list_df_agrupados = list_df

            elif option == 'Semana':
                column_x = 'Week'
                list_df_agrupados = agrupaDados(list_df, [column_x])

            elif option == 'Mês':
                column_x = 'YearMonth'
                list_df_agrupados = agrupaDados(list_df, [column_x])
            
            elif option == 'Ano':
                column_x = 'Year'
                list_df_agrupados = agrupaDados(list_df, [column_x])



            with tab1:
                st.header('Visão Geral dos Dados')

                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    tabs_empresas = st.tabs(list_selected)


                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:

                            st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")
                            st.write(list_df_agrupados[i])

                            figCandlestick = exibirCanddleStick(list_df_agrupados[i], column_x, list_selected[i], title='Gráfico Candlestick da ação', width=1000, height=500, xlabel='Período', ylabel='Valores')
                            
                            df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 7)
                            figCandlestick = adicionarMediaMovel(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 7 dias', color = '#FF0')
                            
                            df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 15)
                            figCandlestick = adicionarMediaMovel(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 15 dias', color = '#323ca8')

                            df_mediamovel = calculaMediaMovel(list_df_agrupados[i], days = 30)
                            figCandlestick = adicionarMediaMovel(figCandlestick, df_mediamovel, x = column_x, y = 'MediaMovel', name= 'Média móvel 30 dias', color = '#a8329b')
                            

                            
                            
                            st.write(figCandlestick)





            with tab2:
                st.header('Análise Estatística')
                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    optionDecompose = st.radio(
                            "Escolha o tipo de decomposição: ",
                            ('Aditiva', 'Multiplicativa'))


                    tabs_empresas = st.tabs(list_selected)
                    

                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:

                            st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")

                            figureBarPlot = exibirGrafico([list_df[i]], type='box', list_tickers = list_selected, x='Year', y='Close', title='Boxplot por ano para análise interquartil', xlabel='Período', ylabel='Valor', width=300, height=400)
                            figureHistogram = exibirGrafico([list_df[i]], type='histogram',list_tickers = list_selected , x='Close', y='Close', title='Histograma com valores de Fechamento', xlabel='Valores', ylabel='Quantidade', width=300, height=400)
                            
                            df_adfuller = calculaEstacionaridade(list_df[i], 'Close')
                            
                            if optionDecompose == 'Aditiva':
                                list_df_decomposition = decompor_serie(list_df[i], 'aditive')

                            else: #Multiplicativa
                                list_df_decomposition = decompor_serie(list_df[i], 'multiplicative')

                            
                            

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

                            st.write(figureDecompose1)
                            st.write(figureDecompose2)
                            st.write(figureDecompose3)

                            

            with tab3:
                st.header('Análise Descritiva')
                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:

                    figureTimeSerie = exibirGrafico(list_df_agrupados, list_selected, type='line', x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação]', xlabel='Período', ylabel='Valor')

                    df_rentabilidade = calculaRentabilidade(list_df_agrupados, list_selected)
                    

                    st.write(figureTimeSerie)
                    
                    c1, c2 = st.columns(2)

                    c1.write('Rentabilidade das ações')
                    c1.write(df_rentabilidade)


            with tab4:
                st.header('Análise Preditiva')
                if len(df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    st.write('Os dados já foram carregados')


        else:
            st.write('A data inicial deve ser menor que a data final e a data inicial deve ser menor que o dia atual')

        



###############################################################################################################

if __name__ == '__main__':

    # transformation
    sidebar_features()

    main_page()