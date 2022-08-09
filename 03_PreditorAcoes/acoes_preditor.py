import streamlit as st
from datetime import date
from PIL import Image
import pandas as pd
import numpy as np

from include.coleta import coletaDados, agrupaDados
from include.graphs import exibirTimeSeries


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


def pages_sidebar():

    list_selected = st.multiselect( 'Selecione a empresa', list_tickers)
    c1, c2 = st.columns(2)

    input_dt_ini = c1.date_input("Data Inicial")
    input_dt_fim = c2.date_input("Data Final")


    tab1, tab2, tab3, tab4 = st.tabs(['Visão Geral dos Dados', 'Análise Estatística', 'Análise Descritiva', 'Análise Preditiva'])

    if len(list_selected) > 0:


        if input_dt_ini < input_dt_fim and input_dt_ini < date.today():

            #Coletando os dados
            list_df = coletaDados(list_selected, interval='1d', start=input_dt_ini.strftime("%Y-%m-%d"), end=input_dt_fim.strftime("%Y-%m-%d"))

            with tab1:
                st.header('Visão Geral dos Dados')

                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    tabs_empresas = st.tabs(list_selected)

                    for i in range(len(tabs_empresas)):
                        with tabs_empresas[i]:
                            st.write(f"Exibindo Dados do Ticker: {list_selected[i]}")
                            st.write(list_df[i])


            with tab2:
                st.header('Análise Estatística')
                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    st.write('Os dados já foram carregados')

                


            with tab3:
                st.header('Análise Descritiva')
                if len(list_df) == 0:
                    st.write('Os dados não foram carregados')
                else:
                    option = st.selectbox( 'Exibir informações por: ', ('Dia', 'Semana', 'Mês', 'Ano')) 
                    
                    figure = 'A minha benga'
                    column_x = 'Date'

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
                    

                    figure = exibirTimeSeries(list_df_agrupados, list_selected, x=column_x, y='Close', title=f'Série Temporal agrupada por {column_x} [Valor de Fechamento da ação]', xlabel='Período', ylabel='Valor')
                    st.write(figure)
                    


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

    pages_sidebar()