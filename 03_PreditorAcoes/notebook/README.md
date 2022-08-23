<h1>PREDITOR DE AÇÕES</h1>

> Realizado por: **Henrique Krupck Secchi**

<h2>SUMÁRIO</h2>

* <a href="#id-1">1) INTRODUÇÃO</a>
	* <a href="#id-1.1">1.1) Definição do problema</a>
	* <a href="#id-1.2">1.2) Objetivos do projeto</a>
	* <a href="#id-1.3">1.3) Conceitos</a>
<br/><br/>

* <a href="#id-2">2) COLETA DE DADOS</a>
<br/><br/>

* <a href="#id-3">3) ANÁLISE DOS DADOS</a>
	* <a href="#id-3.1">3.1) Análise Exploratória</a>
	* <a href="#id-3.2">3.2) Análise Descritiva</a>
		* <a href="#id-3.2.1">3.2.1) Volume</a>
		* <a href="#id-3.2.2">3.2.2) Rentabilidade</a>
<br/><br/>
	
* <a href="#id-4">4) ANÁLISE DE SÉRIES TEMPORAIS</a>
	* <a href="#id-4.1">4.1) Séries Temporais Aditivas e Multiplicativas</a>
	* <a href="#id-4.2">4.2) Descomposição da Série Temporal</a>
	* <a href="#id-4.3">4.3) Estacionaridade</a>
		* <a href="#id-4.3.1">4.3.1) Recapitulando</a>
		* <a href="#id-4.3.2">4.3.2) Verificando a Estacionariedade</a>
		* <a href="#id-4.3.3">4.3.3) O Que São Lags (Defasagens ou Atrasos)?</a>
		* <a href="#id-4.3.4">4.3.4) Autocorrelação</a>
		* <a href="#id-4.3.5">4.3.5) Exibição das Rolling Statistics (Estatísticas Móveis)</a>
		* <a href="#id-4.3.6">4.3.6) Gráficos ACF e PACF</a>
		* <a href="#id-4.3.7">4.3.7) Teste Dickey-Fuller Aumentado</a>
		* <a href="#id-4.3.8">4.3.8) Tipos de Estacionariedade</a>
		* <a href="#id-4.3.9">4.3.9) Transformando uma Série Não Estacionária em Série Estacionária</a>
<br/><br/>

* <a href="#id-5">5) PRÉ-PROCESSAMENTO DOS DADOS</a>
	* <a href="#id-5.1">5.1) Transformação dos Dados</a>
		* <a href="#id-5.1.1">5.1.1) Transformação de Log</a>
		* <a href="#id-5.1.2">5.1.2) Diferenciação</a>
		* <a href="#id-5.1.3">5.1.3) Transformação de Raiz Quadrada</a>
		* <a href="#id-5.1.4">5.1.4) Transformação Box-Cox</a>
	* <a href="#id-5.2">5.2) Suavização(Smoothing)</a>
		* <a href="#id-5.2.1">5.2.1) Smoothing</a>
		* <a href="#id-5.2.2">5.2.2) Média Móvel Simples</a>
		* <a href="#id-5.2.3">5.2.3) Média Móvel Ponderada Exponencial</a>
<br/><br/>

* <a href="#id-6">6) MODELAGEM</a>
	* <a href="#id-6.1">6.1) Conceitos</a>
	* <a href="#id-6.2">6.2) Divisão em Treino e Teste</a>
	* <a href="#id-6.3">6.3) Método Naive</a>
	* <a href="#id-6.4">6.4) Trabalhando com Forecasting mais avançado</a>	
	* <a href="#id-6.5">6.5) Exponential Smoothing</a>
	* <a href="#id-6.6">6.6) Modelos ARIMA</a>
		* <a href="#id-6.6.1">6.6.1) Primeiro Modelo ARIMA</a>
		* <a href="#id-6.6.2">6.6.2) Melhorando os parâmetros P, Q e D</a>
		* <a href="#id-6.6.3">6.6.3) Determinando o valor do Parâmetro d para o modelo ARIMA</a>
		* <a href="#id-6.6.4">6.6.4) Determinando o Valor do Parâmetro p para o Modelo ARIMA</a>
		* <a href="#id-6.6.5">6.6.5) Determinando o Valor do Parâmetro q para o Modelo ARIMA</a>
	* <a href="#id-6.7">6.7) Modelo SARIMA</a>
		* <a href="#id-6.7.1">6.7.1) Seasonal Autoregressive Integrated Moving-Average (SARIMA)</a>
		* <a href="#id-6.7.2">6.7.2) Elementos de Tendência</a>
		* <a href="#id-6.7.3">6.7.3) Elementos de Sazonalidade</a>
		* <a href="#id-6.7.4">6.7.4) Notação SARIMA</a>
		* <a href="#id-6.7.5">6.7.5) Parâmetros SARIMA(3,1,0)(1,1,0)15</a>
		* <a href="#id-6.7.6">6.7.6) Grid Search Método 1 - Stepwise Search</a>
<br/><br/>		
	
* <a href="#id-7">7) FORECASTING</a>
	* <a href="#id-7.1">7.1) Utilizando o modelo SARIMA para prever os próximos 6 meses</a>
<br/><br/>	
	
* <a href="#id-8">8) CONSIDERAÇÕES SOBRE O PROJETO</a>
	* <a href="#id-8.1">8.1) Considerações</a>
	* <a href="#id-8.2">8.2) Streamlit</a>
	* <a href="#id-8.3">8.3) Referências</a>
	* <a href="#id-8.4">8.4) Agradecimentos</a>
<br/><br/>

---
<h2 id="id-1">1) INTRODUÇÃO</h2>
<h3 id="id-1.1">1.1) Definição do problema</h3>

Ações representam partes fracionadas de companhias que possuem capital aberto, em outras palavras, são títulos que são negociados na Bolsa de Valores. As ações se enquadram em três categorias: ON, PN e UNIT. A diferença entre elas é que as ações ordinárias (ON) dão direito a voto nas assembleias da empresa e as ações preferenciais (PN) possuem preferência na distribuição dos resultados. Já as UNITs são formadas pelos dois tipos.

Esse tipo de investimento atrai cada vez mais brasileiros para a Bolsa de Valores. A quantidade de investidores pessoa física operando nesse mercado passou dos 3 milhões em 2020, mesmo diante do cenário de pandemia, e o volume financeiro negociado foi de mais de R$6.4 trilhões no mesmo ano.

Para uma modalidade que vem batendo recordes de pontos com seu principal índice de ações, o Ibovespa, o interesse faz todo sentido. Afinal, para quem quer impulsionar as finanças, bons investimentos sempre são bem-vindos.

No entanto, comprar ações é um desafio, tanto para profissionais que trabalham na área, quanto para pessoas comuns que querem investir seu dinheiro. Este é um mercado cheio de incertezas e o conceito de Entropia se faz fortemente neste âmbito. Identificar padrões matemáticos e traçar tendências são uma ótima forma de tentar identificar como as ações se comportam e como irão se comportar ao longo do tempo.

Além de identificar padrões e tendências, é possível também aplicar técnicas mais avançadas para tentar prever o futuro do mercado financeiro. Técnicas como: modelos ARIMA e Redes Neurais Recorrents (RNNS). Tais técnicas exigem um grau de abstração maior, mas compensam como sendo ferramentas poderosas para auxiliar na tomada de decisão.

<h3 id="id-1.2">1.2) Objetivos do projeto</h3>

Dado o contexto, este projeto tem por objetivo, o desenvolvimento de um modelo capaz de prever o preço das ações em um futuro próximo e determinar se o ativo vai se valorizar ou desvalorizar. 

Os dados serão coletados via API fornecida pelo Yahoo. O projeto também aborda uma análise exploratória e descritiva dos dados utilizando diversas ferramentas e técnicas empregadas no uso de análise de séries temporais.

<h3 id="id-1.3">1.3) Conceitos</h3>

**O que são ações?**

Como citado anteriormente, ações são títulos que representam uma pequena parte do valor das companhias ou sociedades anônimas. Ou seja, uma ação é como se fosse uma pequena fatia de uma empresa.

Quando uma instituição decide expandir seu negócio, muitas vezes necessita buscar mais dinheiro para isso. Portanto, muitas delas se tornam companhias de capital aberto e ofertam suas ações — chamadas também de papéis — no mercado para obter recursos. Dessa forma, qualquer pessoa devidamente registrada na Bolsa de Valores pode adquirir esses títulos, passando a integrar o grupo de acionistas da companhia. Para a empresa que está distribuindo as ações no mercado, os recursos captados poderão ser usados como investimento em novos projetos e também elevarão o valor de mercado da companhia.

Para quem investe, as vantagens também são animadoras. Afinal de contas, comprar ações é a forma mais simples de se tornar sócio de uma empresa. Os acionistas passam a ter direitos e deveres, de acordo com a quantidade de ações que adquiriu.

Isto é, acionistas com maior participação têm mais responsabilidades e, da mesma forma, retornos melhores. Independentemente da quantidade de ações compradas, um acionista pode receber parte dos lucros obtidos pela empresa. Só é preciso lembrar que o valor a receber depende da quantidade de ações que se tem em carteira.

Por outro lado, precisamos destacar que quem investe nesse mercado também está sujeito a ter perdas. É por isso que fazer uma aplicação no Mercado de Ações é considerado um investimento de risco.

Isso porque esse mercado é muito dinâmico, isto é, ele se movimenta diariamente de acordo com o interesse dos investidores. Por isso podemos chamar de investimentos de renda variável. Para algumas pessoas, as variações no preço de uma ação são vistas como um grande problema. Na verdade, o que nem todos sabem é que essas oscilações fazem surgir ótimas oportunidades de investimento.

É claro que saber como lidar com essas altas e baixas é fundamental para potencializar resultados e suavizar os riscos. Investir em ações é uma habilidade que é adquirida com tempo, estudo e prática. E, é claro, que não podemos esquecer de que essas habilidades têm que vir junto do uso de boas análises do mercado, seja no curto ou no longo prazo.

*****

**Importações dos pacotes de bibliotecas**


```python
#Este pacote é bastante útil para realizar as configurações necessárias no momento da publicação do app no servidor do heroku
#!pip install hss
```


```python
# Análise dos dados
import pandas as pd
import numpy as np 
from datetime import timedelta

# Visualização dos dados
import matplotlib.pyplot as plt
import matplotlib as m
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Computação estatística
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

# Imports análise e modelagem de séries temporais
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller

# Imports para análise de dados
import scipy
from scipy.special import inv_boxcox
from scipy.stats import boxcox

# Pacote que fornece a API para comunicação com o Yahoo Finances
import yfinance as yf

# Análise dos resultados
from sklearn.metrics import mean_squared_error 

from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import pmdarima as pm
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing 
from pmdarima.arima.utils import ndiffs
from pandas.plotting import autocorrelation_plot

import warnings
warnings.filterwarnings("ignore")
```

---
<h2 id="id-2">2) COLETA DE DADOS</h2>

Vamos começar pela coleta dos dados. Eu fiz uma função para automatizar o procedimento. A função coleta dados vai receber a lista de tickers. Por exemplo: ['AMZN', 'APPL'], o intervalo e as datas de inicio e final. 
A função retorna cinco dataframes com diferentes informações:
* **df_info**: Informações a respeito da organização como nome, telefone, etc..
* **list_dfs_stock**: Histórico de ações propriamente dito.
* **list_dfs_quartfinancials**: Balanço dos últimos trimestres da empresa.
* **list_dfs_sustainability**: Informações sobre as pontuações de sustentabilidades da organização.
* **list_dfs_news**: Últimas notícias relacionadas ao ativo.

Neste notebook iremos nos concetrar no dataframe `list_dfs_stock`. A análise será focada no histórico das ações.


```python
#Converte valores numérios para datas (Date)
def timeStampToDate(value):
    try:
        date = datetime.datetime.fromtimestamp(value)
        resultado = f'{date.year}/{date.month}/{date.day} {date.hour}:{date.minute}'
        return resultado

    except:
        return '-'
```


```python
#Essa função expande o dataframe em mais colunas, ele adiciona as colunas Year, Month, Day, ..., de maneira individual, possibilitando uma análise mais segmentada. 
def expandirDataFrame(df):
    df.reset_index(inplace=True)

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Week'] = df['Date'].dt.isocalendar().week
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['YearMonth'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m'))
    df['Data'] = df['Date'].dt.strftime('%Y/%m/%d')
    


    dayweek_map = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}

    months_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',12: 'December'}

    df['NameMonths'] = df['Month'].map(months_map)
    df['NameDayOfWeek'] = df['DayOfWeek'].map(dayweek_map)

    return df
```


```python
def coletaDados(list_codigos = [], interval = '1mo', start = '2015-01-01', end='2022-01-01'):
    print('INICIOU COLETA DOS DADOS')

    df_info = pd.DataFrame()
    
    if not isinstance(list_codigos, list):
        aux = list_codigos
        list_codigos = [aux]

    if len(list_codigos) == 0:
        return 'Erro: Insira um código de uma empresa listada.'

    #Declaração das colunas que desejamos obter na aba de informações da organização
    list_columns_info = ['shortName', 'longName', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'country', 'industry', 'financialCurrency',
                    'recommendationKey', 'recommendationMean', 'currentPrice', 'earningsGrowth', 'currentRatio', 'returnOnAssets', 'numberOfAnalystOpinions',
                    'targetMeanPrice', 'market', 'website', 'logo_url',
                    ]

    #Declaração das colunas que desejamos obter na aba de últimas notícias
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
            
            
            ticket = yf.Ticker(codigo)
            aux = ticket.history(interval=interval, start=start, end=end)
            aux['Ticket'] = codigo
            aux = expandirDataFrame(aux)
            aux.dropna(inplace=True)

            list_dfs_stock.append(aux)


            # Info
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


```


```python
#Irei no clássico, aqui vou analisar as ações da PETR4.SA, uma empresa bastante tradicional no Brazil.
list_selected = ['PETR4.SA']
df_info, list_dfs, list_dfs_quartfinancials, list_dfs_sustainability, list_dfs_news = coletaDados(list_selected, interval='1d', start='2016-01-01', end='2022-08-01')
```

    INICIOU COLETA DOS DADOS
    Coletando dados do ticker: PETR4.SA
    Coletando histórico de ações...
    Coletando informações adicionais...
    Coletando histórico dos últimos trimestres...
    Coletando informações de sustentabilidade...
    Coletando últimas notícias...
    Coleta do ticker PETR4.SA concluída.
    ############################
    


```python
df = list_dfs[0]
```

---
<h2 id="id-3">3) ANÁLISE DOS DADOS</h2>

A partir daqui irei começar as análises dos dados. Volto a frizar que este notebook se concentra na análise do histórico dos preços das ações. Não irei realizar análise de notícias, balanços da empresa ou outros dados.

<h3 id="id-3.1">3.1) Análise Exploratória</h3>


```python
#Exibe cabeçalho
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
      <th>Ticket</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Week</th>
      <th>DayOfWeek</th>
      <th>YearMonth</th>
      <th>Data</th>
      <th>NameMonths</th>
      <th>NameDayOfWeek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-04</td>
      <td>3.308906</td>
      <td>3.540580</td>
      <td>3.298833</td>
      <td>3.459998</td>
      <td>45962100</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2016-01-01</td>
      <td>2016/01/04</td>
      <td>January</td>
      <td>Monday</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.485180</td>
      <td>3.525471</td>
      <td>3.334088</td>
      <td>3.364306</td>
      <td>29446700</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>2016-01-01</td>
      <td>2016/01/05</td>
      <td>January</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.288760</td>
      <td>3.293796</td>
      <td>3.223287</td>
      <td>3.223287</td>
      <td>67507200</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>2</td>
      <td>2016-01-01</td>
      <td>2016/01/06</td>
      <td>January</td>
      <td>Wednesday</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.117523</td>
      <td>3.238397</td>
      <td>3.062123</td>
      <td>3.152778</td>
      <td>57387900</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>3</td>
      <td>2016-01-01</td>
      <td>2016/01/07</td>
      <td>January</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.213214</td>
      <td>3.248469</td>
      <td>3.087304</td>
      <td>3.157814</td>
      <td>52100300</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>8</td>
      <td>1</td>
      <td>4</td>
      <td>2016-01-01</td>
      <td>2016/01/08</td>
      <td>January</td>
      <td>Friday</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Exibe shape dos dados (linhas, colunas)
df.shape
```




    (1637, 18)




```python
#Verificando se há valores nulos
df.isnull().sum()
```




    Date             0
    Open             0
    High             0
    Low              0
    Close            0
    Volume           0
    Dividends        0
    Stock Splits     0
    Ticket           0
    Year             0
    Month            0
    Day              0
    Week             0
    DayOfWeek        0
    YearMonth        0
    Data             0
    NameMonths       0
    NameDayOfWeek    0
    dtype: int64




```python
# Verificando metadados (Tipo dos dados em cada coluna)
df.dtypes
```




    Date             datetime64[ns]
    Open                    float64
    High                    float64
    Low                     float64
    Close                   float64
    Volume                    int64
    Dividends               float64
    Stock Splits              int64
    Ticket                   object
    Year                      int64
    Month                     int64
    Day                       int64
    Week                     UInt32
    DayOfWeek                 int64
    YearMonth        datetime64[ns]
    Data                     object
    NameMonths               object
    NameDayOfWeek            object
    dtype: object




```python
# Uma breve análise da descrição dos dados (quantidade, média, desvio padrão, etc...)
df.describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Week</th>
      <th>DayOfWeek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1.637000e+03</td>
      <td>1637.000000</td>
      <td>1637.0</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
      <td>1637.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>11.927866</td>
      <td>12.106600</td>
      <td>11.736593</td>
      <td>11.917909</td>
      <td>6.243152e+07</td>
      <td>0.008674</td>
      <td>0.0</td>
      <td>2018.802077</td>
      <td>6.298717</td>
      <td>15.742822</td>
      <td>25.618204</td>
      <td>2.001222</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.072626</td>
      <td>5.139567</td>
      <td>5.006893</td>
      <td>5.078418</td>
      <td>3.409264e+07</td>
      <td>0.150564</td>
      <td>0.0</td>
      <td>1.911852</td>
      <td>3.387822</td>
      <td>8.743657</td>
      <td>14.803158</td>
      <td>1.408149</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.115283</td>
      <td>2.150537</td>
      <td>2.074991</td>
      <td>2.115283</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>2016.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.811920</td>
      <td>7.932308</td>
      <td>7.685526</td>
      <td>7.801827</td>
      <td>4.160270e+07</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>2017.000000</td>
      <td>3.000000</td>
      <td>8.000000</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>11.954396</td>
      <td>12.198452</td>
      <td>11.743111</td>
      <td>11.915986</td>
      <td>5.559320e+07</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>2019.000000</td>
      <td>6.000000</td>
      <td>16.000000</td>
      <td>25.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>14.994806</td>
      <td>15.246702</td>
      <td>14.809989</td>
      <td>15.005310</td>
      <td>7.523020e+07</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>2020.000000</td>
      <td>9.000000</td>
      <td>23.000000</td>
      <td>38.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>27.360127</td>
      <td>28.223275</td>
      <td>26.733127</td>
      <td>27.807989</td>
      <td>4.902304e+08</td>
      <td>3.715490</td>
      <td>0.0</td>
      <td>2022.000000</td>
      <td>12.000000</td>
      <td>31.000000</td>
      <td>53.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
      <th>Ticket</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Week</th>
      <th>DayOfWeek</th>
      <th>YearMonth</th>
      <th>Data</th>
      <th>NameMonths</th>
      <th>NameDayOfWeek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-04</td>
      <td>3.308906</td>
      <td>3.540580</td>
      <td>3.298833</td>
      <td>3.459998</td>
      <td>45962100</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2016-01-01</td>
      <td>2016/01/04</td>
      <td>January</td>
      <td>Monday</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.485180</td>
      <td>3.525471</td>
      <td>3.334088</td>
      <td>3.364306</td>
      <td>29446700</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>2016-01-01</td>
      <td>2016/01/05</td>
      <td>January</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.288760</td>
      <td>3.293796</td>
      <td>3.223287</td>
      <td>3.223287</td>
      <td>67507200</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>2</td>
      <td>2016-01-01</td>
      <td>2016/01/06</td>
      <td>January</td>
      <td>Wednesday</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.117523</td>
      <td>3.238397</td>
      <td>3.062123</td>
      <td>3.152778</td>
      <td>57387900</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>3</td>
      <td>2016-01-01</td>
      <td>2016/01/07</td>
      <td>January</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.213214</td>
      <td>3.248469</td>
      <td>3.087304</td>
      <td>3.157814</td>
      <td>52100300</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>8</td>
      <td>1</td>
      <td>4</td>
      <td>2016-01-01</td>
      <td>2016/01/08</td>
      <td>January</td>
      <td>Friday</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1632</th>
      <td>2022-07-25</td>
      <td>24.111114</td>
      <td>25.039404</td>
      <td>24.111114</td>
      <td>24.998690</td>
      <td>79106600</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2022</td>
      <td>7</td>
      <td>25</td>
      <td>30</td>
      <td>0</td>
      <td>2022-07-01</td>
      <td>2022/07/25</td>
      <td>July</td>
      <td>Monday</td>
    </tr>
    <tr>
      <th>1633</th>
      <td>2022-07-26</td>
      <td>25.405835</td>
      <td>25.747837</td>
      <td>24.909118</td>
      <td>25.251120</td>
      <td>78360100</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2022</td>
      <td>7</td>
      <td>26</td>
      <td>30</td>
      <td>1</td>
      <td>2022-07-01</td>
      <td>2022/07/26</td>
      <td>July</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>1634</th>
      <td>2022-07-27</td>
      <td>25.487263</td>
      <td>25.625693</td>
      <td>24.933548</td>
      <td>25.527979</td>
      <td>56097200</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2022</td>
      <td>7</td>
      <td>27</td>
      <td>30</td>
      <td>2</td>
      <td>2022-07-01</td>
      <td>2022/07/27</td>
      <td>July</td>
      <td>Wednesday</td>
    </tr>
    <tr>
      <th>1635</th>
      <td>2022-07-28</td>
      <td>25.723408</td>
      <td>26.570270</td>
      <td>25.593122</td>
      <td>26.293411</td>
      <td>114996500</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2022</td>
      <td>7</td>
      <td>28</td>
      <td>30</td>
      <td>3</td>
      <td>2022-07-01</td>
      <td>2022/07/28</td>
      <td>July</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>1636</th>
      <td>2022-07-29</td>
      <td>27.360127</td>
      <td>28.223275</td>
      <td>26.733127</td>
      <td>27.807989</td>
      <td>181480600</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2022</td>
      <td>7</td>
      <td>29</td>
      <td>30</td>
      <td>4</td>
      <td>2022-07-01</td>
      <td>2022/07/29</td>
      <td>July</td>
      <td>Friday</td>
    </tr>
  </tbody>
</table>
<p>1637 rows × 18 columns</p>
</div>




```python
# Um plot inicial para ver a série temporal de maneira gráfica.
df[['Open', 'High', 'Low', 'Close']].plot()
```




    <AxesSubplot:>




    
![png](assets/output_21_1.png)
    


<h3 id="id-3.2">3.2) Análise Descritiva</h3>

Agora que tivemos uma visão geral dos dados e dos metadados, irei fazer uma análise descritiva para entender o comportamento desta ação específica. Abaixo irei criar duas funções: `exibirTimeSeries` e `exibirBarPlot` para auxiliar na exibição dos gráficos.


```python
df.reset_index(inplace=True)
```


```python
def exibirTimeSeries(df, x = 'columnX', y = 'columnY', title = 'Title Default', width = 1000, height = 400, xlabel='xlabel', ylabel='ylabel'):
    fig = px.line(df, x = x, y = y)

    fig.update_layout(
        title=f'<span>{title}</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title=f'<span>{xlabel}</span>'),
        yaxis=dict(title=f'<span>{ylabel}</span>')
    )

    fig.show()
```


```python
def exibirBarPlot(df, x = 'columnX', y = 'columnY', title = 'Title Default', width = 1000, height = 400, xlabel='xlabel', ylabel='ylabel'):
    fig = px.bar(df, x = x, y = y)

    fig.update_layout(
        title=f'<span>{title}</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title=f'<span>{xlabel}</span>'),
        yaxis=dict(title=f'<span>{ylabel}</span>')
    )

    fig.show()
```


```python
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
      <th>Ticket</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Week</th>
      <th>DayOfWeek</th>
      <th>YearMonth</th>
      <th>Data</th>
      <th>NameMonths</th>
      <th>NameDayOfWeek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2016-01-04</td>
      <td>3.308906</td>
      <td>3.540580</td>
      <td>3.298833</td>
      <td>3.459998</td>
      <td>45962100</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2016-01-01</td>
      <td>2016/01/04</td>
      <td>January</td>
      <td>Monday</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2016-01-05</td>
      <td>3.485180</td>
      <td>3.525471</td>
      <td>3.334088</td>
      <td>3.364306</td>
      <td>29446700</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>2016-01-01</td>
      <td>2016/01/05</td>
      <td>January</td>
      <td>Tuesday</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2016-01-06</td>
      <td>3.288760</td>
      <td>3.293796</td>
      <td>3.223287</td>
      <td>3.223287</td>
      <td>67507200</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>2</td>
      <td>2016-01-01</td>
      <td>2016/01/06</td>
      <td>January</td>
      <td>Wednesday</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2016-01-07</td>
      <td>3.117523</td>
      <td>3.238397</td>
      <td>3.062123</td>
      <td>3.152778</td>
      <td>57387900</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>3</td>
      <td>2016-01-01</td>
      <td>2016/01/07</td>
      <td>January</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2016-01-08</td>
      <td>3.213214</td>
      <td>3.248469</td>
      <td>3.087304</td>
      <td>3.157814</td>
      <td>52100300</td>
      <td>0.0</td>
      <td>0</td>
      <td>PETR4.SA</td>
      <td>2016</td>
      <td>1</td>
      <td>8</td>
      <td>1</td>
      <td>4</td>
      <td>2016-01-01</td>
      <td>2016/01/08</td>
      <td>January</td>
      <td>Friday</td>
    </tr>
  </tbody>
</table>
</div>



**<h5 id="id-3.2.1">3.2.1) Volume</h5>**

Primeiro, o atributo Volume. Vejamos o quanto a ação foi negociada ao longo do tempo.


```python
# Obtendo o Somatório do Volume agrupado por Year
df_volume = df.groupby(['Year'], as_index=False)['Volume'].sum()

exibirTimeSeries(df_volume, 'Year', 'Volume', title='Volume de transações ao longo dos anos', ylabel='Volume', xlabel='Anos')
```


    
![png](assets/output_28_0.png)
    



```python
# Obtendo o Somatório do Volume agrupado por YearMonth
df_volume = df.groupby(['YearMonth'], as_index=False)['Volume'].sum()


exibirTimeSeries(df_volume, 'YearMonth', 'Volume', title='Volume de transações ao longo dos anos e meses', ylabel='Volume', xlabel='Anos e Meses')
```


    
![png](assets/output_29_0.png)
    



```python
# Obtendo o Somatório do Volume agrupado por NameMonths, Month
df_volume = df.groupby(['NameMonths', 'Month'], as_index=False)['Volume'].sum().sort_values(by='Month')

exibirBarPlot(df_volume, 'NameMonths', 'Volume', title='Quantidade de Transações por Meses', ylabel='Volume', xlabel='Meses')
```


    
![png](assets/output_30_0.png)
    



```python
# Obtendo o Somatório do Volume agrupado por Week
df_volume = df.groupby(['Week'], as_index=False)['Volume'].sum()

exibirBarPlot(df_volume, 'Week', 'Volume', title='Quantidade de Transações por Semanas do Ano', ylabel='Volume', xlabel='Semanas do Ano')
```


    
![png](assets/output_31_0.png)
    



```python
df_volume = df.groupby(['Day'], as_index=False)['Volume'].sum()

exibirBarPlot(df_volume, 'Day', 'Volume', title='Quantidade de Transações por Dias do Mês', ylabel='Volume', xlabel='Dias do Mês')
```


    
![png](assets/output_32_0.png)
    



```python
# Obtendo o Somatório do Volume agrupado por Day e NameMonths
df_volume = df.groupby(['Day', 'NameMonths'], as_index=False)['Volume'].sum()

df_volume.sort_values(by=['Volume'], ascending=False)[0:15]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Day</th>
      <th>NameMonths</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>252</th>
      <td>22</td>
      <td>February</td>
      <td>770615700</td>
    </tr>
    <tr>
      <th>101</th>
      <td>9</td>
      <td>March</td>
      <td>642090600</td>
    </tr>
    <tr>
      <th>197</th>
      <td>17</td>
      <td>March</td>
      <td>605605800</td>
    </tr>
    <tr>
      <th>280</th>
      <td>24</td>
      <td>May</td>
      <td>592630800</td>
    </tr>
    <tr>
      <th>113</th>
      <td>10</td>
      <td>March</td>
      <td>578786700</td>
    </tr>
    <tr>
      <th>264</th>
      <td>23</td>
      <td>February</td>
      <td>562034900</td>
    </tr>
    <tr>
      <th>29</th>
      <td>3</td>
      <td>March</td>
      <td>553070900</td>
    </tr>
    <tr>
      <th>210</th>
      <td>18</td>
      <td>May</td>
      <td>539557200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>June</td>
      <td>529390100</td>
    </tr>
    <tr>
      <th>89</th>
      <td>8</td>
      <td>March</td>
      <td>524967600</td>
    </tr>
    <tr>
      <th>125</th>
      <td>11</td>
      <td>March</td>
      <td>514287700</td>
    </tr>
    <tr>
      <th>209</th>
      <td>18</td>
      <td>March</td>
      <td>501914200</td>
    </tr>
    <tr>
      <th>103</th>
      <td>9</td>
      <td>November</td>
      <td>472948700</td>
    </tr>
    <tr>
      <th>47</th>
      <td>5</td>
      <td>August</td>
      <td>463633500</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2</td>
      <td>March</td>
      <td>457160000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Obtendo o Somatório do Volume agrupado por NameDayOfWeek, DayOfWeek e ordenado por dias da semana
df_volume = df.groupby(['NameDayOfWeek', 'DayOfWeek'], as_index=False)['Volume'].sum().sort_values(by='DayOfWeek')

exibirBarPlot(df_volume, 'NameDayOfWeek', 'Volume', title='Quantidade de Transações por Dias da Semana', ylabel='Volume', xlabel='Dias da Semana')
```


    
![png](assets/output_34_0.png)
    


**<h5 id="id-3.2.2">3.2.2) Rentabilidade</h5>**


```python
#Rentabilidade é preço atual/ preço anterior * 100 - 100
df[['Rentability']] = df[['Close']] / df[['Close']].shift() * 100 - 100

print('Rentabilidade Total no Período: {}'.format(round(df['Rentability'].sum(), 3)))
print('Rentabilidade Média no Período: {}'.format(round(df['Rentability'].mean(), 3)))
```

    Rentabilidade Total no Período: 290.166
    Rentabilidade Média no Período: 0.177
    


```python
# Exibindo a média de rentablidade das ações agrupadas por Year
df_volume = df.groupby(['Year'], as_index=False)['Rentability'].mean()


exibirTimeSeries(df_volume, 'Year', 'Rentability', title='Rentabilidade em média ao longo dos Anos', ylabel='Média', xlabel='Anos')
```


    
![png](assets/output_37_0.png)
    



```python
# Exibindo a média de rentablidade das ações agrupadas por YearMonth
df_volume = df.groupby(['YearMonth'], as_index=False)['Rentability'].mean()

exibirTimeSeries(df_volume, 'YearMonth', 'Rentability', title='Rentabilidade em média ao longo dos Anos e Meses', ylabel='Média', xlabel='Anos')
```


    
![png](assets/output_38_0.png)
    



```python
# Exibindo a média de rentablidade das ações agrupadas por Rentability
df_volume = df.groupby(['Date'], as_index=False)['Rentability'].mean()


exibirTimeSeries(df_volume, 'Date', 'Rentability', title='Rentabilidade em média ao longo de todo o período', ylabel='Média', xlabel='Anos')
```


    
![png](assets/output_39_0.png)
    



```python
# Exibindo a média de rentablidade das ações agrupadas por NameMonths, Month
df_volume = df.groupby(['NameMonths', 'Month'], as_index=False)['Rentability'].mean().sort_values(by='Month')

exibirBarPlot(df_volume, 'NameMonths', 'Rentability', title='Rentabilidade em média ao longo dos meses', ylabel='Média', xlabel='Anos')
```


    
![png](assets/output_40_0.png)
    


---

<h2 id="id-4">4) ANÁLISE DE SÉRIES TEMPORAIS</h2>


```python
exibirTimeSeries(df, x=df['Date'], y=df['Close'], title='Série Temporal do Valor de Fechamento', xlabel='Período', ylabel='Valor')
```


    
![png](assets/output_42_0.png)
    


O gráfico acima mostra 2 componentes da série: Sazonalidade e Tendência.

* Sazonalidade - o fenômeno se repete em períodos fixos.
* Tendência - ao longo do tempo, a série segue uma tendência de crescimento.

Outro aspecto a considerar é o comportamento cíclico. Isso acontece quando o padrão de subida e descida da série não ocorre em intervalos fixos baseados em calendário. Deve-se tomar cuidado para não confundir efeito "cíclico" com efeito "sazonal".

Então, como diferenciar um padrão "cíclico" versus "sazonal"?

Se os padrões não tiverem frequências fixas baseadas em calendário, será cíclico. Porque, diferentemente da sazonalidade, os efeitos cíclicos são tipicamente influenciados pelos negócios e outros fatores socioeconômicos.

Analisar o gráfico da densidade de observações pode fornecer mais informações sobre a estrutura dos dados. Vamos criar o gráfico:


```python
print('O Skewness do conjunto é: {}'.format(df['Close'].skew()))
plt.figure(figsize=(10, 6))
sns.histplot(df['Close'], kde=True, bins=30)
```

    O Skewness do conjunto é: 0.48566844655584346
    




    <AxesSubplot:xlabel='Close', ylabel='Count'>




    
![png](assets/output_44_2.png)
    


Análise:

* A distribuição não é perfeitamente gaussiana (distribuição normal).
* A distribuição está inclinada para a esquerda.
* As transformações podem ser úteis antes da modelagem.

Vamos agora criar Box Plots para cada ano da série.


```python
# Define a área de plotagem para os subplots (os boxplots)
fig, ax = plt.subplots(figsize=(15,6))

# Cria um box plot para cada ano usando o Seaborn
sns.boxplot(df['Year'], df['Close'], ax = ax)
```




    <AxesSubplot:xlabel='Year', ylabel='Close'>




    
![png](assets/output_46_1.png)
    


Análise:
* Valores medianos ao longo dos anos confirmam uma tendência ascendente.
* Um modelo considerando a sazonalidade pode funcionar bem para prever esta série.

<h3 id="id-4.1">4.1) Séries Temporais Aditivas e Multiplicativas</h3>

Dependendo da natureza da tendência e da sazonalidade, uma série temporal pode ser modelada como aditiva ou multiplicativa, em que cada observação na série pode ser expressa como uma soma ou um produto dos componentes:

* **Séries temporais aditivas**: Valor = Nível Base + Tendência + Sazonalidade + Erro
* **Séries temporais multiplicativas**: Valor = Nível Base x Tendência x Sazonalidade x Erro

<h3 id="id-4.2">4.2) Descomposição da Série Temporal</h3>

- Podemos usar os modelos estatísticos para realizar uma decomposição dessa série cronológica.
- A decomposição de séries temporais é uma tarefa estatística que desconstrói uma série temporal em vários componentes, cada um representando uma das categorias de padrões.
- Com os modelos de estatísticas, poderemos ver a tendência, os componentes sazonais e residuais de nossos dados.

Você pode fazer uma decomposição clássica de uma série temporal, considerando a série como uma combinação aditiva ou multiplicativa do nível base, tendência, índice sazonal e residual.

A função seasonal_decompose do pacote Statsmodels em Python implementa isso convenientemente. Aqui o site do Statsmodels com bastante documentação: https://www.statsmodels.org/


```python
df.index = df['Date']

# Multiplicative Decomposition 
decomposicao_multiplicativa = sm.tsa.seasonal_decompose(df[['Close']], period=50, model = 'multiplicative', extrapolate_trend = 'freq')

# Additive Decomposition
decomposicao_aditiva = sm.tsa.seasonal_decompose(df[['Close']], period=50, model = 'aditive', extrapolate_trend = 'freq')

# Plot
plt.rcParams.update({'figure.figsize': (16,8)})
decomposicao_multiplicativa.plot().suptitle('Decomposição Multiplicativa', fontsize = 18)
decomposicao_aditiva.plot().suptitle('Decomposição Aditiva', fontsize = 18)
plt.show()
```


    
![png](assets/output_50_0.png)
    



    
![png](assets/output_50_1.png)
    


No gráfico acima podemos ver os componentes da série temporal:

**1.** A primeira linha do gráfico mostra os dados ;<br/>
**2.** A segunda linha mostra a tendência do gráfico, que claramente é uma tendência de crescimento, ou seja, o valor de fechamento `Close` tende a crescer ao longo do tempo;<br/>
**3.** A terceira linha mostra a sazonalidade. Claramente temos períodos regulares de aumento e queda;<br/>
**4.** A quarta linha é o componete irregular ou resíduo.

Definir extrapolate_trend = 'freq' cuida de todos os valores ausentes na tendência e nos resíduos no início da série (se existirem, claro).

Se você observar atentamente os resíduos da decomposição aditiva, ela permanece com algum padrão. A decomposição multiplicativa, no entanto, parece bastante aleatória, o que é bom. Então, idealmente, a decomposição multiplicativa deve ser preferida para essa série específica.

A saída numérica da tendência, os componentes sazonais e residuais são armazenados na própria saída decomposicao_multiplicativa. Vamos extraí-los e colocá-los em uma tabela de dados.


```python
# Tipo do objeto
type(decomposicao_multiplicativa)
```




    statsmodels.tsa.seasonal.DecomposeResult




```python
# Concatena o resultado da decomposição da série
dados_serie_reconstruida = pd.concat([decomposicao_multiplicativa.seasonal, 
                                      decomposicao_multiplicativa.trend, 
                                      decomposicao_multiplicativa.resid, 
                                      decomposicao_multiplicativa.observed], axis = 1)

# Define o nome das colunas
dados_serie_reconstruida.columns = ['Sazonalidade', 'Tendência', 'Resíduos', 'Valores_Observados']

# Mostra o resultado
dados_serie_reconstruida.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sazonalidade</th>
      <th>Tendência</th>
      <th>Resíduos</th>
      <th>Valores_Observados</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016-01-04</th>
      <td>1.043234</td>
      <td>1.560684</td>
      <td>2.125100</td>
      <td>3.459998</td>
    </tr>
    <tr>
      <th>2016-01-05</th>
      <td>1.033446</td>
      <td>1.602800</td>
      <td>2.031087</td>
      <td>3.364306</td>
    </tr>
    <tr>
      <th>2016-01-06</th>
      <td>1.023749</td>
      <td>1.644917</td>
      <td>1.914086</td>
      <td>3.223287</td>
    </tr>
    <tr>
      <th>2016-01-07</th>
      <td>1.014643</td>
      <td>1.687034</td>
      <td>1.841859</td>
      <td>3.152778</td>
    </tr>
    <tr>
      <th>2016-01-08</th>
      <td>1.020799</td>
      <td>1.729151</td>
      <td>1.789012</td>
      <td>3.157814</td>
    </tr>
  </tbody>
</table>
</div>



<h3 id="id-4.3">4.3) Estacionaridade</h3>

Uma série temporal estacionária é aquela cujas propriedades estatísticas como média, variância, autocorrelação, etc. são todas constantes ao longo do tempo. A maioria dos métodos de previsão estatística são baseados na suposição de que a série temporal pode ser tornada aproximadamente estacionária (ou seja, "estacionarizada") através do uso de transformações matemáticas. 

Uma série estacionária é relativamente fácil de prever: você simplesmente prevê que suas propriedades estatísticas serão as mesmas no futuro como foram no passado As previsões para a série estacionária podem então ser transformadas, revertendo quaisquer transformações matemáticas usadas anteriormente, para obter previsões para a série original. 

Portanto, encontrar a seqüência de transformações necessárias para estacionar uma série temporal geralmente fornece pistas importantes na busca de um modelo de previsão apropriado. Estacionar uma série temporal por meio de diferenciação (quando necessário) é uma parte importante do processo de ajuste de um modelo ARIMA, conforme discutido nas páginas ARIMA destas notas.

**<h5 id="id-4.3.1">4.3.1) Recapitulando</h5>**

* Uma série temporal é considerada estacionária se suas propriedades estatísticas, como média e variância, permanecerem constantes ao longo do tempo.

* A maioria dos modelos de séries temporais trabalha com o pressuposto de que a série temporal é estacionária. A principal razão para isso é que existem muitas maneiras pelas quais uma série pode ser não estacionária, mas apenas uma para estacionariedade.

* Intuitivamente, podemos dizer que, se uma série temporal tem um comportamento específico ao longo do tempo, há uma probabilidade muito alta de que ela siga o mesmo no futuro.

* Além disso, as teorias relacionadas às séries estacionárias são mais maduras e mais fáceis de implementar em comparação às séries não estacionárias.

A estacionariedade é um importante conceito na modelagem de séries temporais e é caracterizada por uma variável que se comporta de forma aleatória ao longo do tempo ao redor de uma média constante.

Basicamente, séries temporais que possuem tendência e/ou sazonalidade não são estacionárias e é necessário o uso de técnicas adequadas a tal situação.

**<h5 id="id-4.3.2">4.3.2) Verificando a Estacionariedade</h5>**

Podemos verificar a estacionariedade de uma série temporal da seguinte forma:

* **Rolling Statistics (Estatísticas Móveis)**: Podemos criar uma visualização da média móvel e variância móvel (ou desvio padrão, que é a raiz quadrada da variância) e ver se variam com o tempo. A média / variância móvel é, para qualquer instante 't', a média / variância do último ano, ou seja, nos últimos dias e meses.
* **Autocorrelação com Gráficos ACF e PACF**: Se a série temporal for estacionária, os gráficos ACF / PACF (gráficos de autocorrelação da série) mostrarão um padrão específico.
* **Teste Dickey-Fuller**: Este é um dos testes estatísticos para verificar a estacionariedade. Aqui, a hipótese nula é que a série temporal não é estacionária. Os resultados do teste incluem uma estatística de teste e alguns valores críticos para os níveis de confiança das diferenças. Se a 'Estatística de teste' for menor que o 'valor crítico', podemos rejeitar a hipótese nula e dizer que a série é estacionária.

---

**<h5 id="id-4.3.3">4.3.3) O Que São Lags (Defasagens ou Atrasos)?</h5>**

Uma maneira de analisar os dados de séries temporais é plotar cada observação contra outra observação que ocorreu algum tempo antes. Por exemplo, você pode visualizar `yt` contra `yt-1.` Nesse caso, `yt-1` é o atraso da série, o lag.

As correlações associadas aos gráficos de atraso formam o que é chamado de "função de autocorrelação". A autocorrelação é quase a mesma que a correlação de Pearson (que usamos em modelos de Regressão). No entanto, a autocorrelação é a correlação de uma série temporal com uma cópia atrasada (lag, atraso ou defasagem) de si mesma.

A `função de autocorrelação (ACF) `é o principal método na análise de séries temporais para quantificar o nível de correlação entre uma série e seus atrasos. Esse método é bastante semelhante (matematicamente e logicamente) ao coeficiente de correlação de Pearson.

---
**<h5 id="id-4.3.4">4.3.4) Autocorrelação</h5>**

Os modelos estatísticos mais conhecidos e utilizados, como a Regressão Linear e o Regressão Logística, são adequados na modelagem de variáveis em que as observações são independentes. Em uma série temporal, não há como desconsiderar a estrutura de dependência das observações. Por exemplo, a quantidade vendida de um item X em determinado pode estar relacionada com as vendas no mês anterior, que por sua vez pode estar relacionada com o mês `t-2`, e assim por diante.

A autocorrelação é definida como uma observação num determinado instante está relacionada às observações passadas.

As observações podem estar autocorrelacionadas em diversas ordens. A autocorrelação de primeira ordem caracteriza séries onde uma observação está correlacionada com a observação imediatamente anterior (janeiro e dezembro, por exemplo). A autocorrelação de segunda ordem caracteriza séries temporais onde uma observação está correlacionada com as observações a 2 unidades de tempo no passado (janeiro e novembro, por exemplo).

A identificação da autocorrelação é feita através da Função de Autocorrelação (`ACF – Autocorrelation Function`). Além disso, testes como o de Durbin Watson auxiliam na identificação da autocorrelação de primeira ordem.

A autocorrelação é uma ferramenta matemática para encontrar padrões de repetição, como a presença de um sinal periódico obscurecidos pelo ruído. Um diagrama de autocorrelações apresenta os valores de autocorrelação de uma amostra versus o intervalo de tempo em que foi calculado. Autocorrelações devem ser próximas de zero para aleatoriedade. A ocorrência de não estacionariedade é denotada pela lenta queda da `ACF` nos primeiros lags da série. Isto significa que a série deve ser diferenciada, e que um modelo `ARIMA` ou `SARIMA` deve ser aplicado.

Antes de iniciar qualquer modelagem preditiva é necessário verificar se essas propriedades estatísticas são constantes na série temporal:

* Média constante
* Variância constante
* Autocorrelacionada

---

**<h5 id="id-4.3.5">4.3.5) Exibição das Rolling Statistics (Estatísticas Móveis)</h5>**


```python
df_month = df.groupby(['YearMonth'], as_index=False)['Close'].sum()


fig = go.Figure()

fig.add_traces(go.Line(x=df_month['YearMonth'], y=df_month['Close'], name='Original'))

# Determinando estatísticas móveis
rolmean = df_month['Close'].rolling(window = 12).mean()
rolstd = df_month['Close'].rolling(window = 12).std()

fig.add_traces(go.Line(x=df_month['YearMonth'], y=rolmean, name='Média Móvel'))
fig.add_traces(go.Line(x=df_month['YearMonth'], y=rolstd, name='Desvio Padrão'))


fig.update_layout(
        title='<span>Plot das Rolling Statistics (Estatísticas Móveis)</span>', 
        autosize=False,
        width=1200,
        height=500,
        xaxis=dict(title=f'<span>Tempo</span>'),
        yaxis=dict(title=f'<span>Valroes</span>')
    )

fig.show()
```


    
![png](assets/output_56_0.png)
    


Análise:

* Observamos que a média móvel e o desvio padrão não são constantes em relação ao tempo (tendência crescente).
* A série cronológica não é, portanto, estacionária.

**<h5 id="id-4.3.6">4.3.6) Gráficos ACF e PACF</h5>**

Vamos criar os gráficos da função de autocorrelação (ACF) e da função de autocorrelação parcial (PACF).


```python
# Plots
plt.rcParams.update({'figure.figsize': (16,10)})

# Plot do gráfico ACF
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
plt.subplot(211)
plot_acf(df_month['Close'], ax = plt.gca(), lags = 30)

# Plot do gráfico PACF
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html
plt.subplot(212)
plot_pacf(df_month['Close'], ax = plt.gca(), lags = 30)
plt.show()
```


    
![png](assets/output_59_0.png)
    


*Interpretação dos Gráficos:*

No gráfico, o eixo vertical indica a autocorrelação e o horizontal a defasagem.

A área sombreada em azul indica onde é significativamente diferente de zero. Como é possível ver na imagem, temos diversos valores ACF (barras verticais) acima do limite da área sombreada em azul. Nesses casos, a autocorrelação é diferente de zero, indicando que a série não é aleatória – conforme o esperado.

Algumas barras verticais estão dentro do limite da área sombreada em azul, Ou seja, a autocorrelação entre a série com alguns de seus lags é igual a zero, indicando que não há correlação.

Em termos simples: a área sombreada em azul aponta a significância. Se ultrapassa é porque tem correlação.

Cada barra no gráfico ACF representa o nível de correlação entre a série e seus atrasos em ordem cronológica. A área sombreada em azul indica se o nível de correlação entre a série e cada atraso é significativo ou não.

Testando a hipótese nula de que a correlação do atraso com a série é igual a zero, podemos rejeitá-la sempre que o nível de correlação estiver acima ou abaixo da área sombreada em azul com um nível de significância de 5%.

Caso contrário, sempre que a correlação estiver dentro da área sombreada em azul, deixamos de rejeitar a hipótese nula e, portanto, podemos ignorar esses atrasos (ou assumir que não há correlação significativa entre eles e a série).

O PACF é apenas uma visualização parcial do ACF.

*Análise:*

* Se a série temporal for estacionária, os gráficos do ACF / PACF mostrarão uma "queda rápida na correlação" após um pequeno atraso entre os pontos. Não é o caso em nossos gráficos. A queda lenda (redução do tamanho das barras) indica que essa série não é estacionária).
* Os dados da nossa série não são estacionários, pois um número alto de observações anteriores está correlacionado com valores futuros.
* Intervalos de confiança são desenhados na área azul clara. Por padrão, isso é definido como um intervalo de confiança de 95%, sugerindo que os valores de correlação fora desta área provavelmente são uma correlação e não um acaso estatístico.
* Teremos que transformar essa série em estacionária antes de criar um modelo preditivo.

---

**<h5 id="id-4.3.7">4.3.7) Teste Dickey-Fuller Aumentado</h5>**

* A intuição por trás do teste é que, se a série for integrada, o nível de atraso da série `y (t-1)` não fornecerá informações relevantes na previsão da mudança em `y (t)`.
* Hipótese nula: a série temporal não é estacionária.
* Rejeitar a hipótese nula (ou seja, um valor-p abaixo de 0.05) indicará estacionaridade.


```python
# Teste Dickey-Fuller

# Print
print('\nResultado do Teste Dickey-Fuller:\n')

# Teste
dfteste = adfuller(df['Close'], autolag = 'AIC')

# Formatando a saída
dfsaida = pd.Series(dfteste[0:4], index = ['Estatística do Teste',
                                           'Valor-p',
                                           'Número de Lags Consideradas',
                                           'Número de Observações Usadas'])

# Loop por cada item da saída do teste
for key,value in dfteste[4].items():
    dfsaida['Valor Crítico (%s)'%key] = value

# Print
print (dfsaida)
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -0.456832
    Valor-p                            0.900169
    Número de Lags Consideradas       12.000000
    Número de Observações Usadas    1624.000000
    Valor Crítico (1%)                -3.434383
    Valor Crítico (5%)                -2.863321
    Valor Crítico (10%)               -2.567718
    dtype: float64
    

Análise:

* O Valor-p é maior que 0.05. Não temos evidências para rejeitar a hipótese nula de que a série não é estacionária.

Abaixo irei criar uma função que executa o teste de estacionaridade e pode ser aplicada a qualquer série para testar se ela é ou não estacionária.

Se a série não for estacionária, teremos que aplicar transformações antes da modelagem.


```python
def testaEstacionaridade(df, column, autolag = 'AIC'):
    
    # Teste Dickey-Fuller:
    # Print
    print('\nResultado do Teste Dickey-Fuller:\n')

    # Teste
    dfteste = adfuller(df[column], autolag = autolag)

    # Formatando a saída
    dfsaida = pd.Series(dfteste[0:4], index = ['Estatística do Teste',
                                               'Valor-p',
                                               'Número de Lags Consideradas',
                                               'Número de Observações Usadas'])

    # Loop por cada item da saída do teste
    for key, value in dfteste[4].items():
        dfsaida['Valor Crítico (%s)'%key] = value

    # Print
    print (dfsaida)
    
    # Testa o valor-p
    print ('\nConclusão:')
    if dfsaida[1] > 0.05:
        print('\nO valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.')
        print('Essa série provavelmente não é estacionária.')
    else:
        print('\nO valor-p é menor que 0.05 e, logo, temos fortes evidências para rejeitar a hipótese nula.')
        print('Essa série provavelmente é estacionária.')

```


```python
testaEstacionaridade(df, 'Close')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -0.456832
    Valor-p                            0.900169
    Número de Lags Consideradas       12.000000
    Número de Observações Usadas    1624.000000
    Valor Crítico (1%)                -3.434383
    Valor Crítico (5%)                -2.863321
    Valor Crítico (10%)               -2.567718
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    

**<h5 id="id-4.3.8">4.3.8) Tipos de Estacionariedade</h5>**

Agora que identificamos que a série não é estacionária, temos algumas coisas para fazer. Teremos que transformar esta série em uma série estacionária, mas antes disso tudo, me deixe explicar mais sobre séries estacionárias e seus tipos de estacionaridades. Existem três tipos de estacionariedade, vejamos cada uma delas:

* **Estacionaridade Estrita**: Uma série estacionária estrita satisfaz a definição matemática de um processo estacionário. Para uma série estacionária estrita, a média, variância e covariância não são funções do tempo. O objetivo é converter uma série não estacionária em uma série estacionária estrita para fazer previsões.

* **Estacionaridade de Tendência**: Uma série que não possui raiz unitária, mas exibe uma tendência, é chamada de série estacionária de tendência. Uma vez removida a tendência, a série resultante será estritamente estacionária. O teste KPSS (Kwiatkowski-Phillips-Schmidt-Shin) classifica uma série como estacionária na ausência de raiz da unidade. Isso significa que a série pode ser estacionária estrita ou estacionária de tendência.

* **Estacionaridade Diferencial**: Uma série temporal que pode ser tornada estritamente estacionária pela diferenciação é do tipo estacionária diferencial. O teste ADF (Augmented Dickey Fuller) também é conhecido como teste de estacionariedade diferencial.

É sempre melhor aplicar os dois testes, para ter certeza de que a série é realmente estacionária.

---

**<h5 id="id-4.3.9">4.3.9) Transformando uma Série Não Estacionária em Série Estacionária</h5>**

Se a série temporal não for estacionária, podemos frequentemente transformá-la em estacionária com uma das técnicas seguintes (ou combinações delas).

**1.** Transformações de potência. Aplicamos uma transformação matemática aos dados visando remover padrões e transformar a série em estacionária. As transformações de potência mais comuns são a de `log`, `raiz` quadrada e `Box-Cox`.<br/>
**2.** Podemos diferenciar os dados. Isto é, dada a série Yt, criamos a nova série: `Y(i) = Y(i) - Y(i-1)` <br/>
Os dados diferenciados conterão um ponto a menos que os dados originais. Embora você possa diferenciar os dados mais que uma vez, uma diferenciação é geralmente suficiente.<br/>
**3.** Se os dados tiverem uma tendência, podemos ajustar algum tipo de curva aos dados e depois então modelar os resíduos daquele ajuste. Desde que o propósito do ajuste é simplesmente remover tendências de longo prazo, um ajuste simples, tal como uma linha reta, é tipicamente usado. <br/>
**4.** Para dados negativos, você pode adicionar uma constante adequada para tornar todos os dados positivos antes de aplicar a transformação. Esta constante pode então ser subtraída do modelo para obter valores previstos (i.e., ajustados) e previsões para pontos futuros. <br/>

As técnicas acima são dirigidas para gerarem séries com localizações e escala constantes. 

**Portanto,** As principais técnicas para aplicar estacionaridade são:

**Tipos de Transformações**

- Transformação de log
- Transformação exponencial
- Transformação Box Cox
- Transformação da raiz quadrada

**Remoção de Tendência**

- Smoothing (alisamento ou suavização) é usada para remover a tendência da série, calculando médias contínuas ao longo das janelas de tempo.

Mas as técnicas acima não funcionam em todos os casos, principalmente nos de alta sazonalidade. Para esses casos, outras técnicas podem ser usadas:

**Diferenciação**

- Nesta técnica, calculamos a diferença da observação em um determinado instante com a do instante anterior.

**Decomposição**

- Nesta abordagem, a tendência e a sazonalidade são modeladas separadamente e a parte restante da série é retornada.

---
<h2 id="id-5">5) PRÉ-PROCESSAMENTO DOS DADOS</h2>

<h3 id="id-5.1">5.1) Transformação dos Dados</h3>


```python
df_transformed = df[['Close']].copy()
df_transformed.reset_index(inplace=True)
```


```python
df_transformed.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-04</td>
      <td>3.459998</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.364306</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.223287</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.152778</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.157814</td>
    </tr>
  </tbody>
</table>
</div>



Vamos começar pela transformação de log no nosso conjunto de dados.

**<h5 id="id-5.1.1">5.1.1) Transformação de Log</h5>**

Séries temporais com uma distribuição exponencial podem ser linearizadas usando o logaritmo dos valores. Isso é chamado de transformação de log. Você com certeza lembra do que é logaritmo pois estudou isso no ensino fundamental. :-)

As transformações de log são populares em dados de séries temporais, pois são eficazes na remoção da variação exponencial.

É importante observar que esta operação assume que os valores são positivos e diferentes de zero. É comum transformar observações adicionando uma constante fixa para garantir que todos os valores de entrada atendam a esse requisito. Por exemplo: serie_transformada_y = log(constante + x)


```python
# Vamos aplicar uma transformação de log usando np.log() e gravamos o resultado em uma nova coluna do nosso dataset
df_transformed['CloseLog'] = np.log(df_transformed['Close'])
df_transformed.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Close</th>
      <th>CloseLog</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-04</td>
      <td>3.459998</td>
      <td>1.241268</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.364306</td>
      <td>1.213222</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.223287</td>
      <td>1.170402</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.152778</td>
      <td>1.148284</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.157814</td>
      <td>1.149880</td>
    </tr>
  </tbody>
</table>
</div>




```python
exibirTimeSeries(df_transformed, x='Date', y='Close', title='Série Temporal Normal', xlabel='Período', ylabel='Valores')
exibirTimeSeries(df_transformed, x='Date', y='CloseLog', title='Série Temporal com Transformação de Log', xlabel='Período', ylabel='Valores')
```






```python
print('O Skewness da Série Normal é de: {}'.format(df_transformed['Close'].skew()))
print('O Skewness da Série Log é de: {}'.format(df_transformed['CloseLog'].skew()))
plt.figure(figsize=(10,6))
sns.histplot(df_transformed['CloseLog'], kde=True)
```

    O Skewness da Série Normal é de: 0.48566844655584346
    O Skewness da Série Log é de: -0.7516635560986136
    




    <AxesSubplot:xlabel='CloseLog', ylabel='Count'>




    
![png](assets/output_75_2.png)
    



```python
testaEstacionaridade(df_transformed, 'CloseLog')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -2.629697
    Valor-p                            0.087013
    Número de Lags Consideradas       16.000000
    Número de Observações Usadas    1620.000000
    Valor Crítico (1%)                -3.434393
    Valor Crítico (5%)                -2.863326
    Valor Crítico (10%)               -2.567721
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    

Análise:

* Embora a Série pareça estar visualmente mais linear, vemos que a transformação log não mudou muita coisa;
* Pelo histograma percebemos que a transformação log se aproximou mais de zero, mas não foi um valor considerável.

---

**<h5 id="id-5.1.2">5.1.2) Diferenciação</h5>**


```python
# Aplicando Diferenciação - Y(i) = Y(i) - Y(i-1)
# Gravamos a série diferenciada no próprio dataset
df_transformed['CloseDiff'] = df_transformed['Close'] - df_transformed['Close'].shift(1)
df_transformed['CloseDiffLog'] = df_transformed['CloseLog'] - df_transformed['CloseLog'].shift(1)
df_transformed.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Close</th>
      <th>CloseLog</th>
      <th>CloseDiff</th>
      <th>CloseDiffLog</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-04</td>
      <td>3.459998</td>
      <td>1.241268</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.364306</td>
      <td>1.213222</td>
      <td>-0.095691</td>
      <td>-0.028046</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.223287</td>
      <td>1.170402</td>
      <td>-0.141019</td>
      <td>-0.042820</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.152778</td>
      <td>1.148284</td>
      <td>-0.070509</td>
      <td>-0.022118</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.157814</td>
      <td>1.149880</td>
      <td>0.005036</td>
      <td>0.001596</td>
    </tr>
  </tbody>
</table>
</div>




```python
exibirTimeSeries(df_transformed, x='Date', y='Close', title='Série Temporal Normal', xlabel='Período', ylabel='Valores')
exibirTimeSeries(df_transformed, x='Date', y='CloseDiff', title='Série Temporal com Transformação de Diferenciação', xlabel='Período', ylabel='Valores')
exibirTimeSeries(df_transformed, x='Date', y='CloseDiffLog', title='Série Temporal com Transformação de Log e de Diferenciação', xlabel='Período', ylabel='Valores')
```








```python
print('O Skewness da Série Normal é de: {}'.format(df_transformed['Close'].skew()))
print('O Skewness da Série Log é de: {}'.format(df_transformed['CloseLog'].skew()))
print('O Skewness da Série Dif é de: {}'.format(df_transformed['CloseDiff'].skew()))
print('O Skewness da Série Dif Log é de: {}'.format(df_transformed['CloseDiffLog'].skew()))
plt.figure(figsize=(10,6))
sns.histplot(df_transformed['CloseDiffLog'], kde=True)
```

    O Skewness da Série Normal é de: 0.48566844655584346
    O Skewness da Série Log é de: -0.7516635560986136
    O Skewness da Série Dif é de: -1.378432024940676
    O Skewness da Série Dif Log é de: -1.4067466966409898
    




    <AxesSubplot:xlabel='CloseDiffLog', ylabel='Count'>




    
![png](assets/output_81_2.png)
    



```python
df_transformed.dropna(inplace=True)
```


```python
testaEstacionaridade(df_transformed, 'CloseDiff')
testaEstacionaridade(df_transformed, 'CloseDiffLog')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste           -1.086264e+01
    Valor-p                         1.433407e-19
    Número de Lags Consideradas     1.100000e+01
    Número de Observações Usadas    1.624000e+03
    Valor Crítico (1%)             -3.434383e+00
    Valor Crítico (5%)             -2.863321e+00
    Valor Crítico (10%)            -2.567718e+00
    dtype: float64
    
    Conclusão:
    
    O valor-p é menor que 0.05 e, logo, temos fortes evidências para rejeitar a hipótese nula.
    Essa série provavelmente é estacionária.
    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste           -1.016319e+01
    Valor-p                         7.414998e-18
    Número de Lags Consideradas     1.500000e+01
    Número de Observações Usadas    1.620000e+03
    Valor Crítico (1%)             -3.434393e+00
    Valor Crítico (5%)             -2.863326e+00
    Valor Crítico (10%)            -2.567721e+00
    dtype: float64
    
    Conclusão:
    
    O valor-p é menor que 0.05 e, logo, temos fortes evidências para rejeitar a hipótese nula.
    Essa série provavelmente é estacionária.
    

Análise:
* Visualizando o gráfico vemos que a Série perdeu o componente tendência, isso é bom, porém a distribuição se distanciou de uma distribuição normal e ficou pior do que antes.

**<h5 id="id-5.1.3">5.1.3) Transformação de Raiz Quadrada</h5>**

Uma série temporal que tem uma tendência quadrática de crescimento pode ser linearizada calculando sua raiz quadrada.

É possível que uma companhia mostre um crescimento quadrático. Se esse for o caso, poderíamos esperar que uma transformação de raiz quadrada para reduzir a tendência de crescimento seja linear e alterar a distribuição de observações para talvez ser quase gaussiana.

O exemplo abaixo executa uma raiz quadrada do conjunto de dados e plota os resultados.


```python
# Transformação de Raiz Quadrada com np.sqrt()
df_transformed['CloseSqrt'] = np.sqrt(df_transformed['Close'])
```


```python
exibirTimeSeries(df_transformed, x='Date', y='CloseSqrt', title='Série Temporal com Transformação de Raiz Quadrada', xlabel='Período', ylabel='Valores')
```




```python
print('O Skewness da Série Sqrt é de: {}'.format(df_transformed['CloseSqrt'].skew()))
plt.figure(figsize=(10,6))
sns.histplot(df_transformed['CloseSqrt'], kde=True)
```

    O Skewness da Série Sqrt é de: -0.07338622754323652
    




    <AxesSubplot:xlabel='CloseSqrt', ylabel='Count'>




    
![png](assets/output_88_2.png)
    



```python
testaEstacionaridade(df_transformed, 'CloseSqrt')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -1.341364
    Valor-p                            0.610042
    Número de Lags Consideradas       16.000000
    Número de Observações Usadas    1619.000000
    Valor Crítico (1%)                -3.434396
    Valor Crítico (5%)                -2.863327
    Valor Crítico (10%)               -2.567721
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    

Análise:
* Podemos ver qua a série manteve o componente tendência, mas a distribuição ficou mais normal segundo a métrica `skewness`. Contudo, o histograma possui dois picos.

--- 

**<h5 id="id-5.1.4">5.1.4) Transformação Box-Cox</h5>**

A transformação de raiz quadrada e a transformação de log pertencem a uma classe de transformações denominadas transformações de potência.

A transformação Box-Cox é um método de transformação de dados configurável que suporta a raiz quadrada e a transformação de log, bem como um conjunto de transformações relacionadas.

Mais do que isso, pode ser configurado para avaliar um conjunto de transformações automaticamente e selecionar o melhor ajuste. Pode ser pensado como uma ferramenta elétrica para resolver mudanças baseadas em energia em suas séries temporais. A série resultante pode ser mais linear e a distribuição resultante mais gaussiana ou uniforme, dependendo do processo que a gerou.

A biblioteca scipy.stats fornece uma implementação da transformação Box-Cox. A função boxcox() usa um argumento, chamado lambda, que controla o tipo de transformação a ser executada.

Abaixo estão alguns valores comuns para lambda

- **lambda = -1.** é uma transformação recíproca.
- **lambda = -0.5** é uma transformação de raiz quadrada recíproca.
- **lambda = 0.0** é uma transformação de log.
- **lambda = 0.5** é uma transformação de raiz quadrada.
- **lambda = 1.0** não é transformação.

Podemos definir o parâmetro lambda como None (o padrão) e deixar a função encontrar um valor ajustado estatisticamente.


```python
# Aplicando Transformação Box-Cox
#df_transformed['CloseBoxCox'] = boxcox(df_transformed['Close'], lmbda = 0.0)
df_transformed['CloseBoxCox'], lambda_value = boxcox(df_transformed['Close'])

print(f'O valor escolhido para lambda: {lambda_value}')
df_transformed.head()
```

    O valor escolhido para lambda: 0.5375663824983984
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Close</th>
      <th>CloseLog</th>
      <th>CloseDiff</th>
      <th>CloseDiffLog</th>
      <th>CloseSqrt</th>
      <th>CloseBoxCox</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.364306</td>
      <td>1.213222</td>
      <td>-0.095691</td>
      <td>-0.028046</td>
      <td>1.834205</td>
      <td>1.710924</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.223287</td>
      <td>1.170402</td>
      <td>-0.141019</td>
      <td>-0.042820</td>
      <td>1.795352</td>
      <td>1.629660</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.152778</td>
      <td>1.148284</td>
      <td>-0.070509</td>
      <td>-0.022118</td>
      <td>1.775606</td>
      <td>1.588411</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.157814</td>
      <td>1.149880</td>
      <td>0.005036</td>
      <td>0.001596</td>
      <td>1.777024</td>
      <td>1.591371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01-11</td>
      <td>3.067160</td>
      <td>1.120752</td>
      <td>-0.090654</td>
      <td>-0.029128</td>
      <td>1.751331</td>
      <td>1.537746</td>
    </tr>
  </tbody>
</table>
</div>




```python
exibirTimeSeries(df_transformed, x='Date', y='CloseBoxCox', title=f'Série Temporal com Transformação BoxCox e valor Lambda: {lambda_value}', xlabel='Período', ylabel='Valores')
```




```python
print('O Skewness da Série BoxCox é de: {}'.format(df_transformed['CloseBoxCox'].skew()))
plt.figure(figsize=(10,6))
sns.histplot(df_transformed['CloseBoxCox'], kde=True)
```

    O Skewness da Série BoxCox é de: -0.028237015449523208
    




    <AxesSubplot:xlabel='CloseBoxCox', ylabel='Count'>




    
![png](assets/output_95_2.png)
    


Análise:

A execução do exemplo gerou o valor lambda de 0.362. Podemos ver que isso está mais próximo de um valor lambda de 0.5, resultando em uma tendência de transformação de raiz quadrada.


```python
testaEstacionaridade(df_transformed, 'CloseBoxCox')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -1.259377
    Valor-p                            0.647546
    Número de Lags Consideradas       16.000000
    Número de Observações Usadas    1619.000000
    Valor Crítico (1%)                -3.434396
    Valor Crítico (5%)                -2.863327
    Valor Crítico (10%)               -2.567721
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    


```python
df_transformed['CloseBoxCoxDiff'] = df_transformed['CloseBoxCox'] - df_transformed['CloseBoxCox'].shift(1)
df_transformed.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Close</th>
      <th>CloseLog</th>
      <th>CloseDiff</th>
      <th>CloseDiffLog</th>
      <th>CloseSqrt</th>
      <th>CloseBoxCox</th>
      <th>CloseBoxCoxDiff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>3.364306</td>
      <td>1.213222</td>
      <td>-0.095691</td>
      <td>-0.028046</td>
      <td>1.834205</td>
      <td>1.710924</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>3.223287</td>
      <td>1.170402</td>
      <td>-0.141019</td>
      <td>-0.042820</td>
      <td>1.795352</td>
      <td>1.629660</td>
      <td>-0.081264</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>3.152778</td>
      <td>1.148284</td>
      <td>-0.070509</td>
      <td>-0.022118</td>
      <td>1.775606</td>
      <td>1.588411</td>
      <td>-0.041248</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>3.157814</td>
      <td>1.149880</td>
      <td>0.005036</td>
      <td>0.001596</td>
      <td>1.777024</td>
      <td>1.591371</td>
      <td>0.002960</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01-11</td>
      <td>3.067160</td>
      <td>1.120752</td>
      <td>-0.090654</td>
      <td>-0.029128</td>
      <td>1.751331</td>
      <td>1.537746</td>
      <td>-0.053625</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_transformed.dropna(inplace=True)
testaEstacionaridade(df_transformed, 'CloseBoxCoxDiff')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste           -1.014156e+01
    Valor-p                         8.394348e-18
    Número de Lags Consideradas     1.500000e+01
    Número de Observações Usadas    1.619000e+03
    Valor Crítico (1%)             -3.434396e+00
    Valor Crítico (5%)             -2.863327e+00
    Valor Crítico (10%)            -2.567721e+00
    dtype: float64
    
    Conclusão:
    
    O valor-p é menor que 0.05 e, logo, temos fortes evidências para rejeitar a hipótese nula.
    Essa série provavelmente é estacionária.
    

---

<h3 id="id-5.2">5.2) Suavização(Smoothing)</h3>

**<h5 id="id-5.2.1">5.2.1) Smoothing</h5>**

Smoothing (Suavização ou Alisamento) em séries temporais é um conjunto de métodos para suavizar séries temporais eliminando "saltos". Existem várias maneiras de fazer isso. Talvez o mais fácil seja calcular a média móvel simples (Simple Moving Average).

A suavização é basicamente uma técnica usada para ver a tendência de longo prazo nos dados, diminuindo os efeitos dos componentes periódicos / sazonais dos dados. Basicamente, usamos suavização quando queremos remover as flutuações nos dados e focamos apenas em preservar as tendências de longo prazo.

A suavização é uma técnica aplicada às séries temporais para remover a variação granular entre as etapas do tempo.

O objetivo de suavizar é remover o ruído e expor melhor o sinal dos processos. As médias móveis são um tipo simples e comum de suavização usado na análise de séries temporais e na previsão de séries temporais.

O cálculo de uma média móvel envolve a criação de uma nova série em que os valores são compostos da média de observações brutas na série temporal original. 

A suavização da média móvel (Moving Average Smoothing) é uma técnica eficaz na previsão de séries temporais também, ou seja, pode ser usado para preparação de dados, engenharia de recursos e até diretamente para fazer previsões.

Uma média móvel requer que você especifique um tamanho de janela chamado largura da janela. Isso define o número de observações brutas usadas para calcular o valor da média móvel.

A parte "móvel" na média móvel refere-se ao fato de que a janela definida pela largura da janela é deslizada ao longo da série temporal para calcular os valores médios na nova série.

Vejamos como isso funciona.


```python
df_smoothing = df_transformed[['Date', 'CloseBoxCox']].copy()
df_smoothing.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>CloseBoxCox</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>1.629660</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>1.588411</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>1.591371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01-11</td>
      <td>1.537746</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-01-12</td>
      <td>1.366038</td>
    </tr>
  </tbody>
</table>
</div>



**<h5 id="id-5.2.2">5.2.2) Média Móvel Simples</h5>**


```python
# Primeiro, vamos calcular a média da série (essa não é a média móvel, mas sim a média total)
df_smoothing['CloseBoxCox'].mean()
```




    5.024846733184257




```python
# Vamos criar uma cópia da série original pois isso será importante mais tarde
df_smoothing_cp = df_smoothing.copy()
```


```python
# Agora definimos uma janela de 12 meses da série temporal para calcular a média móvel
# Vamos gravar o resultado em outra coluna no próprio dataset
df_smoothing_cp['CloseSmoothing'] = df_smoothing_cp['CloseBoxCox'].rolling(window = 7).mean()
```


```python
df_smoothing_cp.head(15)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>CloseBoxCox</th>
      <th>CloseSmoothing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>1.629660</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>1.588411</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>1.591371</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01-11</td>
      <td>1.537746</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-01-12</td>
      <td>1.366038</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016-01-13</td>
      <td>1.283588</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016-01-14</td>
      <td>1.415886</td>
      <td>1.487529</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016-01-15</td>
      <td>1.251378</td>
      <td>1.433489</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016-01-18</td>
      <td>1.129615</td>
      <td>1.367946</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016-01-19</td>
      <td>1.082417</td>
      <td>1.295238</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016-01-20</td>
      <td>1.003428</td>
      <td>1.218907</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016-01-21</td>
      <td>1.027665</td>
      <td>1.170568</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016-01-22</td>
      <td>0.996471</td>
      <td>1.129552</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016-01-26</td>
      <td>0.922520</td>
      <td>1.059071</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016-01-27</td>
      <td>1.051728</td>
      <td>1.030549</td>
    </tr>
  </tbody>
</table>
</div>



Agora temos duas colunas e alguns valores NaN na coluna das médias móveis. Isso é normal e esperado, afinal, calculamos a média de 12 valores consecutivos "deslizando" a janela pela série e para alguns valores (os primeiros da série) não teremos como calcular a média dos 12 valores anteriores e assim eles ficam como NaN. Ou seja, perdemos registros da série ao aplicar esta técnica de suavização.


```python
df_smoothing_cp.dropna(inplace=True)
```


```python
fig = go.Figure()

fig.add_traces(go.Line(x=df['Date'], y=df['Close'], name='Original'))
fig.add_traces(go.Line(x=df_smoothing_cp['Date'], y=df_smoothing_cp['CloseBoxCox'], name='Transformação Box Cox'))
fig.add_traces(go.Line(x=df_smoothing_cp['Date'], y=df_smoothing_cp['CloseSmoothing'], name='Transformação Smoothing'))


fig.update_layout(
        title='<span>Plot das Transformações</span>', 
        autosize=False,
        width=1200,
        height=500,
        xaxis=dict(title=f'<span>Tempo</span>'),
        yaxis=dict(title=f'<span>Valroes</span>')
    )

fig.show()
```




```python
testaEstacionaridade(df=df_smoothing_cp, column='CloseSmoothing')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -1.181297
    Valor-p                            0.681589
    Número de Lags Consideradas       25.000000
    Número de Observações Usadas    1603.000000
    Valor Crítico (1%)                -3.434436
    Valor Crítico (5%)                -2.863345
    Valor Crítico (10%)               -2.567731
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    

**<h5 id="id-5.2.3">5.2.3) Média Móvel Ponderada Exponencial</h5>**

- Para superar o problema de escolher uma janela definida na média móvel, podemos usar a média móvel ponderada exponencial
- Adotamos uma "média móvel ponderada", em que valores mais recentes recebem um peso maior.
- Pode haver muitas técnicas para atribuir pesos. Uma popular é a média móvel ponderada exponencialmente em que os pesos são atribuídos a todos os valores anteriores com um fator de redução.

A função ewm() do Pandas permite aplicar esse método com facilidade.


```python
# Aplicando suavização exponencial
# Observe que estamos aplicando a suavização à série original (antes de aplicar a suavização anterior)
df_smoothing['CloseExp'] = df_smoothing['CloseBoxCox'].ewm(alpha = 0.5, adjust = True).mean()
df_smoothing.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>CloseBoxCox</th>
      <th>CloseExp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>2016-01-06</td>
      <td>1.629660</td>
      <td>1.629660</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-07</td>
      <td>1.588411</td>
      <td>1.602161</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01-08</td>
      <td>1.591371</td>
      <td>1.595995</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01-11</td>
      <td>1.537746</td>
      <td>1.564929</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-01-12</td>
      <td>1.366038</td>
      <td>1.462276</td>
    </tr>
  </tbody>
</table>
</div>




```python

fig = go.Figure()

fig.add_traces(go.Line(x=df['Date'], y=df['Close'], name='Original'))
fig.add_traces(go.Line(x=df_smoothing['Date'], y=df_smoothing['CloseBoxCox'], name='Transformação Box Cox'))
fig.add_traces(go.Line(x=df_smoothing['Date'], y=df_smoothing['CloseExp'], name='Transformação Exponencial'))


fig.update_layout(
        title='<span>Plot das Transformações</span>', 
        autosize=False,
        width=1200,
        height=500,
        xaxis=dict(title=f'<span>Tempo</span>'),
        yaxis=dict(title=f'<span>Valroes</span>')
    )

fig.show()
```




```python
testaEstacionaridade(df=df_smoothing, column='CloseExp')
```

    
    Resultado do Teste Dickey-Fuller:
    
    Estatística do Teste              -1.234464
    Valor-p                            0.658597
    Número de Lags Consideradas       15.000000
    Número de Observações Usadas    1619.000000
    Valor Crítico (1%)                -3.434396
    Valor Crítico (5%)                -2.863327
    Valor Crítico (10%)               -2.567721
    dtype: float64
    
    Conclusão:
    
    O valor-p é maior que 0.05 e, logo, não temos evidências o suficiente para rejeitar a hipótese nula.
    Essa série provavelmente não é estacionária.
    

Análise:
* Com os métodos de Smoothing não conseguimos tornar a série estacionária. Portanto, iremos continuar utilizando a série obtida com os métodos de BoxCox e Diferenciação.

---
<h2 id="id-6">6) MODELAGEM</h2>

<h3 id="id-6.1">6.1) Conceitos</h3>

A partir de agora utilizaremos as previsões de séries temporais, uma habilidade valiosa e importante em praticamente qualquer área de negócio.

**Por que Forecasting é Importante?**

A previsão de séries temporais (chamado Forecasting) é uma área importante do aprendizado de máquina que geralmente é negligenciada.

É importante porque existem muitos problemas de previsão que envolvem um componente de tempo. Esses problemas são negligenciados porque é esse componente do tempo que dificulta o manuseio dos dados de séries temporais.

**O Tempo**

O tempo desempenha um papel básico, e muitas vezes irrelevante, nos conjuntos de dados que usamos em Machine Learning de forma tradicional (qualquer coisa que não seja série temporal).

São feitas previsões para novos dados quando o resultado real pode não ser conhecido até alguma data futura. O futuro está sendo previsto, mas todas as observações anteriores são quase sempre tratadas igualmente. Talvez com algumas dinâmicas temporais muito pequenas para superar a ideia de `desvio de conceito`, como usar apenas o último ano de observações em vez de todos os dados disponíveis.

Um conjunto de dados de séries temporais é diferente.

As séries temporais adicionam uma dependência explícita da ordem entre as observações: uma dimensão temporal.

Essa dimensão adicional é uma restrição e uma estrutura que fornece uma fonte de informações adicionais. E muito, muito valiosa.

**Descrevendo vs. Prevendo**

Temos objetivos diferentes, dependendo de estarmos interessados em entender um conjunto de dados ou fazer previsões.

A compreensão de um conjunto de dados, chamado análise de séries temporais, pode ajudar a fazer melhores previsões, mas não é necessária e pode resultar em um grande investimento técnico em tempo e experiência, não diretamente alinhados com o resultado desejado, que está prevendo o futuro.

Na modelagem descritiva ou análise de séries temporais, uma série temporal é modelada para determinar seus componentes em termos de padrões sazonais, tendências, relação a fatores externos e similares. Por outro lado, a previsão de séries temporais usa as informações em uma série temporal (talvez com informações adicionais) para prever valores futuros dessa série.

**Análise de Séries Temporais**

Ao usar estatísticas clássicas, a principal preocupação é a análise de séries temporais.

A análise de séries temporais envolve o desenvolvimento de modelos que melhor capturam ou descrevem uma série temporal observada para entender as causas. Este campo de estudo busca o "porquê" por trás de um conjunto de dados de séries temporais.

Isso geralmente envolve fazer suposições sobre a forma dos dados e decompor as séries temporais.

A qualidade de um modelo descritivo é determinada por quão bem ele descreve todos os dados disponíveis e a interpretação que fornece para melhor informar o domínio do problema.

O objetivo principal da análise de séries temporais é desenvolver modelos matemáticos que forneçam descrições plausíveis a partir de dados de amostra.

Isso é o que chamamos de Modelagem Estatística.

**Previsão de Séries Temporais**

Fazer previsões sobre o futuro é chamado de extrapolação no tratamento estatístico clássico de dados de séries temporais.

Os campos mais modernos se concentram no tópico e se referem a ele como previsão de séries temporais.

A previsão envolve ajustar os modelos aos dados históricos e usá-los para prever observações futuras.

Uma distinção importante na previsão é que o futuro está completamente indisponível e só deve ser estimado a partir do que já aconteceu.

O objetivo da análise de séries temporais é geralmente duplo: entender ou modelar os mecanismos estocásticos que dão origem a uma série observada e prever os valores futuros de uma série com base no histórico dessa série.

Isso é o que chamamos de Modelagem Preditiva.


---

<h3 id="id-6.2">6.2) Divisão em Treino e Teste</h3>

Para séries temporais devemos dividir os dados de treino e testes de maneira cronológica, afinal de contas, queremos prever diversos valores ao longo do período.

Para isso, irei pegar os dados inferiores a três meses para realizar o treinamento e os dados dos últimos três meses para testes. 


```python
df_treino = df_transformed.loc[df_transformed['Date'] <= '2022-05-01', ['Date', 'CloseBoxCox']]
df_valid = df_transformed.loc[df_transformed['Date'] > '2022-05-01', ['Date', 'CloseBoxCox']]

df_treino.columns = ['Date', 'Close']
df_valid.columns = ['Date', 'Close']

df_treino.index = df_treino['Date'].values
df_valid.index = df_valid['Date'].values

df_treino.drop(columns=['Date'], inplace=True)
df_valid.drop(columns=['Date'], inplace=True)


df_treino['Close Transformed'] = df_treino['Close'].apply(lambda x: inv_boxcox(x, lambda_value))
df_valid['Close Transformed'] = df_valid['Close'].apply(lambda x: inv_boxcox(x, lambda_value))
```


```python
fig = go.Figure()

fig.add_traces(go.Line(x=df_treino.index, y=df_treino['Close'], name='Dados de Treino'))
fig.add_traces(go.Line(x=df_valid.index, y=df_valid['Close'], name='Dados de Teste'))

fig.update_layout(
        title='<span>Plot dos dados divididos em Treino e Teste</span>', 
        autosize=False,
        width=1200,
        height=500,
        xaxis=dict(title=f'<span>Tempo</span>'),
        yaxis=dict(title=f'<span>Valroes</span>')
    )

fig.show()
```



<h3 id="id-6.3">6.3) Método Naive</h3>

Técnica de estimativa na qual os dados reais do último período são usados como previsão desse período, sem ajustá-los ou tentar estabelecer fatores causais. É usado apenas para comparação com as previsões geradas pelas melhores técnicas (sofisticadas).

Naive = ingênuo

Não há técnica avançada aqui e apenas usamos como ponto de partida. Qualquer modelo mais avançado deve apresentar resultados superiores ao Método Naive.


```python
# Criamos um array com os valores da variável target em treino
array_count_treino = np.asarray(df_treino['Close'])
array_count_treino
```




    array([1.62965953, 1.58841138, 1.59137131, ..., 7.93105349, 7.96601918,
           7.96951032])




```python
# Previsão

# Veja como o método é mesmo Naive
# Os dados reais (de treino) são usados como previsão para os dados de validação, 
# sem ajustá-los ou tentar estabelecer fatores causais.

# Sim, isso é o Método Naive!
df_valid['Pred Naive'] = array_count_treino[len(array_count_treino) - 1] 
```


```python
# Colocamos lado a lado, valor real e valor "previsto"
df_valid.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close</th>
      <th>Close Transformed</th>
      <th>Pred Naive</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-05-02</th>
      <td>7.917037</td>
      <td>21.906765</td>
      <td>7.96951</td>
    </tr>
    <tr>
      <th>2022-05-03</th>
      <td>7.964273</td>
      <td>22.104057</td>
      <td>7.96951</td>
    </tr>
    <tr>
      <th>2022-05-04</th>
      <td>8.277731</td>
      <td>23.433954</td>
      <td>7.96951</td>
    </tr>
    <tr>
      <th>2022-05-05</th>
      <td>8.267530</td>
      <td>23.390112</td>
      <td>7.96951</td>
    </tr>
    <tr>
      <th>2022-05-06</th>
      <td>8.444784</td>
      <td>24.157362</td>
      <td>7.96951</td>
    </tr>
  </tbody>
</table>
</div>




```python
def exibirResultados(df_treino, df_valid, colum): 
    # Define valor real e valor previsto
    y_true = df_valid['Close Transformed']
    y_pred = df_valid[colum]

    # Calcula o erro usando RMSE (Root Mean Squared Error)
    metrica_rmse = np.sqrt(mean_squared_error(y_true, y_pred)) 
    print(f'O Resultado com a Métrica RMSE foi de: {metrica_rmse}')


    fig = go.Figure()

    fig.add_traces(go.Line(x=df_treino.index, y=df_treino['Close Transformed'], name='Dados de Treino'))
    fig.add_traces(go.Line(x=df_valid.index, y=df_valid['Close Transformed'], name='Dados de Teste'))
    fig.add_traces(go.Line(x=df_valid.index, y=df_valid[colum], name='Valores Previstos'))

    fig.update_layout(
            title='<span>Previsão</span>', 
            autosize=False,
            width=1200,
            height=500,
            xaxis=dict(title=f'<span>Tempo</span>'),
            yaxis=dict(title=f'<span>Valores</span>')
        )

    fig.show()
```


```python
df_valid['Pred Naive'] = df_valid['Pred Naive'].apply(lambda x: inv_boxcox(x, lambda_value))

exibirResultados(df_treino.loc[df_treino.index >= '2020-01-01'], df_valid, 'Pred Naive')
```

    O Resultado com a Métrica RMSE foi de: 2.2383937890998995
    



---

<h3 id="id-6.4">6.4) Trabalhando com Forecasting mais avançado</h3>

A técnica anterior foi uma forma de apresentar o modelo mais básico possível, só para termos uma idéia de como os dados se comportarão no futuro. A partir de agora irei aplicar outros modelos com técnicas avançadas de Forecasting.

Para fazer previsões com séries temporais temos diversos algoritmos divididos nestas categorias principais:


**- Modelos de Regressão de Séries Temporais**

O conceito básico é prever a série temporal de interesse y supondo que ela tenha uma relação linear com outras séries temporais x.

Por exemplo, podemos desejar prever vendas mensais y usando o gasto total com publicidade x como um preditor. Ou podemos prever a demanda diária de eletricidade y usando temperatura x1 e o dia da semana x2 como preditores.

A variável y às vezes também é chamada de variável regressante, dependente ou explicada. As variáveis preditoras x às vezes também são chamados de regressores, variáveis independentes ou explicativas. 


**- Exponential Smoothing**

A "suavização exponencial" foi proposta no final da década de 1950 (Brown, 1959; Holt, 1957; Winters, 1960) e motivou alguns dos métodos de previsão mais bem-sucedidos. As previsões produzidas usando métodos de suavização exponencial são médias ponderadas de observações passadas, com os pesos decaindo exponencialmente à medida que as observações "envelhecem". Em outras palavras, quanto mais recente a observação, maior o peso associado. Essa estrutura gera previsões confiáveis rapidamente e para uma ampla gama de séries temporais, o que é uma grande vantagem e de grande importância para muitas aplicações comerciais.


**- Modelos ARIMA (Autoregressive Integrated Moving Average)**

Os modelos ARIMA fornecem outra abordagem para a previsão de séries temporais. A suavização exponencial e os modelos ARIMA são as duas abordagens mais usadas para previsão de séries temporais e fornecem abordagens complementares. Embora os modelos de suavização exponencial sejam baseados em uma descrição da tendência e da sazonalidade nos dados, os modelos ARIMA visam descrever as correlações automáticas nos dados.


**- Modelos de Regressão Dinâmica**

Os modelos de Regressão de Séries Temporais, Exponential Smoothing e ARIMA, permitem a inclusão de informações de observações anteriores de uma série, mas não a inclusão de outras informações que também possam ser relevantes. Por exemplo, os efeitos de feriados, atividade da concorrência, mudanças na lei, economia em geral ou outras variáveis externas podem explicar algumas das variações históricas e levar a previsões mais precisas. 


**- Modelos Hierárquicos ou de Séries Agrupadas**

As séries temporais geralmente podem ser desagregadas naturalmente por vários atributos de interesse. Por exemplo, o número total de bicicletas vendidas por um fabricante de bicicletas pode ser desagregado por tipo de produto, como bicicletas comuns, mountain bikes, bicicletas infantis e híbridos. Cada um deles pode ser desagregado em categorias mais refinadas. Por exemplo, as bicicletas híbridas podem ser divididas em bicicletas urbanas, de transporte, conforto e trekking, e assim por diante. Essas categorias são aninhadas nas categorias de grupos maiores e, portanto, a coleção de séries temporais segue uma estrutura de agregação hierárquica. Portanto, nos referimos a eles como "séries temporais hierárquicas".

Séries temporais hierárquicas geralmente surgem devido a divisões geográficas. Por exemplo, o total de vendas de bicicletas pode ser desagregado por país, depois dentro de cada país por estado, dentro de cada estado por região e assim por diante até o nível da tomada.


**- Métodos Avançados de Previsão de Séries Temporais**

Aqui nós temos técnicas de Combinações, Backcasting, Intervalos Para Agregações e Deep Learning (especialmente com modelos LSTM).

--- 

<h3 id="id-6.5">6.5) Exponential Smoothing</h3>

A suavização exponencial é um método de previsão de séries temporais para dados univariados.

Métodos de séries temporais, como a família de métodos Box-Jenkins ARIMA, desenvolvem um modelo em que a previsão é uma soma linear ponderada de observações ou atrasos (lags) recentes.

Os métodos de previsão de suavização exponencial são semelhantes, pois uma previsão é uma soma ponderada de observações passadas, mas o modelo usa explicitamente um peso decrescente exponencialmente para observações passadas. Especificamente, observações passadas são ponderadas com uma proporção que diminui geometricamente.

As previsões produzidas usando métodos de suavização exponencial são médias ponderadas de observações passadas, com os pesos decaindo exponencialmente à medida que as observações envelhecem. Em outras palavras, quanto mais recente a observação, maior o peso associado.

Os métodos de suavização exponencial podem ser considerados uma alternativa à popular classe de métodos Box-Jenkins ARIMA para previsão de séries temporais.

Coletivamente, os métodos às vezes são chamados de modelos ETS, referindo-se à modelagem explícita de Erro, Tendência e Sazonalidade.


**Tipos de Suavização Exponencial**

Existem três tipos principais de métodos de previsão de séries temporais de suavização exponencial:

Um método simples que não assume estrutura sistemática, uma extensão que lida explicitamente com as tendências e a abordagem mais avançada que adiciona suporte à sazonalidade. Vamos definir cada um deles.


**Suavização Exponencial Simples**

Suavização exponencial simples, o SES, é um método de previsão de séries temporais para dados univariados sem tendência ou sazonalidade.

Requer um único parâmetro, chamado alfa (a), também chamado de fator de suavização ou coeficiente de suavização.

Este parâmetro controla a taxa na qual a influência das observações em etapas anteriores decai exponencialmente. Alfa geralmente é definido como um valor entre 0 e 1. Valores grandes significam que o modelo presta atenção principalmente às observações passadas mais recentes, enquanto valores menores significam que mais da história é levada em consideração ao fazer uma previsão.

Um valor próximo a 1 indica aprendizado rápido (ou seja, apenas os valores mais recentes influenciam as previsões), enquanto um valor próximo a 0 indica aprendizado lento (observações anteriores têm uma grande influência nas previsões).


**Suavização Exponencial Dupla**

A suavização exponencial dupla é uma extensão da suavização exponencial que adiciona explicitamente suporte para tendências na série temporal univariada.

Além do parâmetro alfa para controlar o fator de suavização, um fator de suavização adicional é adicionado para controlar a deterioração da influência da mudança na tendência chamada beta (b).

O método suporta tendências que mudam de maneiras diferentes: um aditivo e um multiplicativo, dependendo se a tendência é linear ou exponencial, respectivamente.

A suavização exponencial dupla com uma tendência aditiva é classicamente chamada de modelo de tendência linear de Holt, homenagem ao desenvolvedor do método, Charles Holt.

- Tendência aditiva: Suavização exponencial dupla com uma tendência linear.
- Tendência multiplicativa: Suavização exponencial dupla com uma tendência exponencial.

Para previsões de longo alcance (várias etapas), a tendência pode continuar irrealisticamente. Como tal, pode ser útil diminuir a tendência ao longo do tempo.


**Suavização Exponencial Tripla**

A suavização exponencial tripla é uma extensão da suavização exponencial que adiciona explicitamente suporte à sazonalidade à série temporal univariada.

Às vezes, esse método é chamado de suavização exponencial de Holt-Winters, homenagem aos dois colaboradores do método: Charles Holt e Peter Winters.

Além dos fatores de suavização alfa e beta, é adicionado um novo parâmetro chamado gama (g) que controla a influência no componente sazonal.

Como na tendência, a sazonalidade pode ser modelada como um processo aditivo ou multiplicativo para uma mudança linear ou exponencial na sazonalidade.

- Sazonalidade aditiva: suavização exponencial tripla com uma sazonalidade linear.
- Sazonalidade multiplicativa: Suavização exponencial tripla com uma sazonalidade exponencial.

A suavização exponencial tripla é a variação mais avançada da suavização exponencial e, através da configuração, também pode desenvolver modelos de suavização exponencial dupla e única.


```python
# Versão 1 do modelo - Simple Exponential Smoothing
# https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.SimpleExpSmoothing.html

# A função SimpleExpSmoothing() recebe os dados de treino no formato de array numpy
# A função fit() faz o treinamento

# O hiperparâmetro smoothing_level define o nível de suavização exponencial na série
# O hiperparâmetro optimized define se teremos ou não otimização 

# Versão 1 do modelo - Simple Exponential Smoothing 
modelo_v1 = SimpleExpSmoothing(np.asarray(df_treino['Close'])).fit(smoothing_level = 0.8, optimized = True) 
```


```python
# Previsões com o Modelo
df_valid['Exp Smoothing V1'] = modelo_v1.forecast(len(df_valid)) 
```


```python
# Colocamos lado a lado, valor real e valor "previsto"
df_valid.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close</th>
      <th>Close Transformed</th>
      <th>Pred Naive</th>
      <th>Exp Smoothing V1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-05-02</th>
      <td>7.917037</td>
      <td>21.906765</td>
      <td>22.12598</td>
      <td>7.967466</td>
    </tr>
    <tr>
      <th>2022-05-03</th>
      <td>7.964273</td>
      <td>22.104057</td>
      <td>22.12598</td>
      <td>7.967466</td>
    </tr>
    <tr>
      <th>2022-05-04</th>
      <td>8.277731</td>
      <td>23.433954</td>
      <td>22.12598</td>
      <td>7.967466</td>
    </tr>
    <tr>
      <th>2022-05-05</th>
      <td>8.267530</td>
      <td>23.390112</td>
      <td>22.12598</td>
      <td>7.967466</td>
    </tr>
    <tr>
      <th>2022-05-06</th>
      <td>8.444784</td>
      <td>24.157362</td>
      <td>22.12598</td>
      <td>7.967466</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_valid['Exp Smoothing V1'] = df_valid['Exp Smoothing V1'].apply(lambda x: inv_boxcox(x, lambda_value))

exibirResultados(df_treino.loc[df_treino.index >= '2020-01-01'], df_valid, 'Exp Smoothing V1')
```

    O Resultado com a Métrica RMSE foi de: 2.245379017702317
    



---

O primeiro modelo obteve o resultado de 0.3523 enquanto que esse modelo obteve o resultado de 0.3533, ou seja, os resultados pioraram. Vamos aplicar outros modelos para tentar melhorar este resultado.


```python
# Versão 2 do modelo - Double Exponential Smoothing 
# https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing.html

# Observe que estamos usando a função ExponentialSmoothing().
# Ao usar o hiperparâmetro trend, definimos o método Double Exponential Smoothing.
# Ao usar o hiperparâmetro seasonal, definimos o método Triple Exponential Smoothing.

# Vamos usar o Double. Como temos sazonalidade, não faz muito sentido usar o Triple.
# Escolhi a série aditiva
modelo_v2 = ExponentialSmoothing(np.asarray(df_treino['Close']), trend = 'additive').fit(smoothing_level = 0.8, optimized = True) 
```


```python
# Previsões com o Modelo
df_valid['Exp Smoothing V2'] = modelo_v2.forecast(len(df_valid)) 

# Colocamos lado a lado, valor real e valor "previsto"
df_valid.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close</th>
      <th>Close Transformed</th>
      <th>Pred Naive</th>
      <th>Exp Smoothing V1</th>
      <th>Exp Smoothing V2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-05-02</th>
      <td>7.917037</td>
      <td>21.906765</td>
      <td>22.12598</td>
      <td>22.117419</td>
      <td>7.972520</td>
    </tr>
    <tr>
      <th>2022-05-03</th>
      <td>7.964273</td>
      <td>22.104057</td>
      <td>22.12598</td>
      <td>22.117419</td>
      <td>7.976564</td>
    </tr>
    <tr>
      <th>2022-05-04</th>
      <td>8.277731</td>
      <td>23.433954</td>
      <td>22.12598</td>
      <td>22.117419</td>
      <td>7.980608</td>
    </tr>
    <tr>
      <th>2022-05-05</th>
      <td>8.267530</td>
      <td>23.390112</td>
      <td>22.12598</td>
      <td>22.117419</td>
      <td>7.984651</td>
    </tr>
    <tr>
      <th>2022-05-06</th>
      <td>8.444784</td>
      <td>24.157362</td>
      <td>22.12598</td>
      <td>22.117419</td>
      <td>7.988695</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_valid['Exp Smoothing V2'] = df_valid['Exp Smoothing V2'].apply(lambda x: inv_boxcox(x, lambda_value))

exibirResultados(df_treino.loc[df_treino.index >= '2020-01-01'], df_valid, 'Exp Smoothing V2')
```

    O Resultado com a Métrica RMSE foi de: 1.8699059554187247
    



Tivemos uma melhora razoável aqui, mas o modelo ainda está longe do ideal, vamos tentar aplicar outros métodos a partir de agora.

---

<h3>6.6) Modelos ARIMA</h3>

Em Estatística e Econometria, e em particular na análise de séries temporais, um modelo de média móvel integrada auto-regressiva (ARIMA) é uma generalização de um modelo de média móvel auto-regressiva (ARMA). 

Ambos os modelos são ajustados a dados de séries temporais para melhor entender os dados ou para prever pontos futuros na série (previsão). Os modelos ARIMA são aplicados em alguns casos em que os dados mostram evidências de não estacionariedade, onde uma etapa inicial de diferenciação (correspondente à parte "integrada" do modelo) pode ser aplicada uma ou mais vezes para eliminar a não estacionariedade. 

A parte AR do ARIMA indica que a variável de interesse em evolução é regredida com seus próprios valores defasados (isto é, anteriores). A parte MA indica que o erro de regressão é na verdade uma combinação linear de termos de erro cujos valores ocorreram contemporaneamente e em vários momentos no passado. O I (para "integrado") indica que os valores dos dados foram substituídos pela diferença entre seus valores e os valores anteriores (e esse processo de diferenciação pode ter sido executado mais de uma vez). O objetivo de cada um desses recursos é fazer com que o modelo ajuste os dados da melhor maneira possível.

Modelos ARIMA não sazonais são geralmente designados ARIMA(p, d, q), em que os parâmetros p, d e q são números inteiros não negativos, p é a ordem (número de intervalos de tempo) do modelo autoregressivo, d é o grau de diferenciação (o número de vezes que os dados tiveram valores passados subtraídos) e q é a ordem do modelo de média móvel. 

Modelos ARIMA sazonais são geralmente designados ARIMA (p, d, q) (P, D, Q) m, em que m refere-se ao número de períodos em cada season e os maiúsculos P, D, Q referem-se ao autorregressivo, diferenciado, e termos da média móvel da parte sazonal do modelo ARIMA.

Quando dois dos três termos são zeros, o modelo pode ser referido com base no parâmetro diferente de zero, eliminando "AR", "I" ou "MA" da sigla que descreve o modelo. Por exemplo, ARIMA (1,0,0) é AR (1), ARIMA (0,1,0) é I (1) e ARIMA (0,0,1) é MA (1).

**<h5 id="id-6.6.1">6.6.1) Primeiro Modelo ARIMA</h5>**

Vamos criar nosso primeiro Modelo ARIMA. Para começar vamos criar um modelo simples, treiná-los e fazer previsões, em seguida vamos explorar os detalhes de Modelos ARIMA, como interpretar o resultado, os resíduos e melhorar o modelo.


```python
# Cria o Modelo ARIMA

# Definimos:

# p = 2
# d = 1
# q = 0

# Aqui o valor q é zero, pois é apenas o modelo AR. Na sequência eu explico porque.

# Modelo
modelo_AR = ARIMA(df_treino['Close'], order = (2, 1, 0))
```

Realizamos todas essas etapas de diferenciação e outras transformações para descobrir os coeficientes do modelo ARIMA. 

'I' no ARIMA significa Integração, que leva em consideração o número de dados diferenciados necessários para se tornar a série estacionária (ou seja, o Modelo ARIMA faz todo o trabalho). 

Realizamos essas etapas de diferenciação no início para encontra o valor ideal de "I". De fato, você deve comparar modelos diferentes com valores diferentes dessas variáveis para obter o melhor modelo.

O Pré-Processamento que fazemos nas séries temporais é para encontrar os melhores valores de p, d e q que colocamos aqui: order = (2, 1, 0).

Portanto, treinamos o modelo com TODOS os dados, a série inteira (dados de treino).


```python
# Treinamento
modelo_v1 = modelo_AR.fit(disp = -1) 

# Forecast
# O parâmetro alfa representa o intervalo de confiança, nesse caso, 95%
fc, se, conf = modelo_v1.forecast(len(df_valid), alpha = 0.05) 
```


```python
# Previsões
fc[0:10]
```




    array([7.97400826, 7.97801386, 7.98206174, 7.98610039, 7.99014016,
           7.99417974, 7.99821934, 8.00225894, 8.00629854, 8.01033814])




```python
# Erro
se[0:10]
```




    array([0.10741929, 0.14759733, 0.18001899, 0.20733847, 0.23147169,
           0.25331417, 0.27341755, 0.29214075, 0.30973422, 0.32638068])




```python
# Coeficientes
conf[0:10]
```




    array([[7.76347033, 8.1845462 ],
           [7.6887284 , 8.26729931],
           [7.62923101, 8.33489247],
           [7.57972446, 8.39247633],
           [7.53646399, 8.44381634],
           [7.49769309, 8.49066639],
           [7.4623308 , 8.53410789],
           [7.42967359, 8.57484429],
           [7.39923063, 8.61336645],
           [7.37064376, 8.65003252]])




```python
df_valid['ARIMA V1'] = fc

df_limites = pd.DataFrame()
df_limites['Limite Inferior'] = conf[:, 0]
df_limites['Limite Superior'] = conf[:, 1]
df_limites.index = df_valid.index


df_valid['ARIMA V1'] = df_valid['ARIMA V1'].apply(lambda x: inv_boxcox(x, lambda_value))
df_limites['Limite Inferior'] = df_limites['Limite Inferior'].apply(lambda x: inv_boxcox(x, lambda_value))
df_limites['Limite Superior'] = df_limites['Limite Superior'].apply(lambda x: inv_boxcox(x, lambda_value))
```


```python
def exibirResultadosComMargem(df_treino, df_valid, df_limites, coluna_pred):
    # Define valor real e valor previsto
    y_true = df_valid['Close Transformed']
    y_pred = df_valid[coluna_pred]

    # Calcula o erro usando RMSE (Root Mean Squared Error)
    metrica_rmse = np.sqrt(mean_squared_error(y_true, y_pred)) 
    print(f'O Resultado com a Métrica RMSE foi de: {metrica_rmse}')


    fig = go.Figure()

    fig.add_traces(go.Line(x=df_treino.index, y=df_treino['Close Transformed'], name='Dados de Treino'))
    fig.add_traces(go.Line(x=df_valid.index, y=df_valid['Close Transformed'], name='Dados de Teste'))
    fig.add_traces(go.Line(x=df_valid.index, y=df_valid[coluna_pred], name='Valores Previstos'))


    fig.add_traces(go.Scatter(x=df_limites.index, y=df_limites['Limite Inferior'].values, name='Margem Inferior', fill='tonexty', line = dict(color='#ccc')))
    fig.add_traces(go.Scatter(x=df_limites.index, y=df_limites['Limite Superior'].values, name='Margem Superior', fill='tonexty', line = dict(color='#ccc')))


    fig.update_layout(
            title='<span>Previsão com o modelo ARIMA</span>', 
            autosize=False,
            width=1200,
            height=500,
            xaxis=dict(title=f'<span>Tempo</span>'),
            yaxis=dict(title=f'<span>Valores</span>')
        )

    fig.show()
```


```python
exibirResultadosComMargem(df_treino, df_valid, df_limites, 'ARIMA V1')
```

    O Resultado com a Métrica RMSE foi de: 1.865998042891108
    



**<h5 id="id-6.6.2">6.6.2) Melhorando os parâmetros P, Q e D</h5>**

O que significam p, d e q no modelo ARIMA?

Um modelo ARIMA requer 3 parâmetros:

- param q: (int) Ordem do modelo MA.
- param p: (int) Ordem do modelo de AR.
- param d: (int) Número de vezes que os dados precisam ser diferenciados.

Nesta aula, vamos estudar como determinar o valor desses 3 parâmetros.

**<h5 id="id-6.6.3">6.6.3) Determinando o valor do Parâmetro d para o modelo ARIMA</h5>**

O objetivo da diferenciação é tornar a série temporal estacionária.

Mas você precisa ter cuidado para não superestimar a série. Por isso, uma série super diferenciada ainda pode ser estacionária, o que, por sua vez, afetará os parâmetros do modelo.

Então, como determinar a ordem correta de diferenciação?

A ordem correta de diferenciação é a diferenciação mínima necessária para obter uma série quase estacionária que circula em torno de uma média definida e o gráfico ACF chega a zero rapidamente.

Se as autocorrelações forem positivas para muitos atrasos (10 ou mais), a série precisará ser diferenciada. Por outro lado, se a autocorrelação lag 1 em si for muito negativa, a série provavelmente será super diferenciada.

Se não for possível realmente decidir entre duas ordens de diferenciação, então escolha a ordem que apresenta o menor desvio padrão na série diferenciada.

Vamos ver como fazer isso com um exemplo.

Primeiro, vou verificar se a série é estacionária usando o teste Augmented Dickey Fuller (adfuller()), do pacote statsmodels ( que já usamos em várias aulas até aqui).

Por quê?

Porque você precisa diferenciar apenas se a série não for estacionária. Senão, nenhuma diferenciação é necessária, ou seja, d = 0.

A hipótese nula do teste ADF é que a série temporal não é estacionária. Portanto, se o valor-p do teste for menor que o nível de significância (0,05), você rejeitará a hipótese nula e poderá inferir que a série temporal é realmente estacionária.

Portanto, se o valor-p > 0,05, prosseguimos em busca da ordem da diferenciação. 

Vamos aplicar o Teste ADF mais uma vez em nossa série:


```python
# Teste ADF
resultado = adfuller(df_treino['Close'])
print('Estatística ADF: %f' % resultado[0])
print('Valor-p: %f' % resultado[1])
```

    Estatística ADF: -1.848043
    Valor-p: 0.356884
    

O valor-p é maior que 0.05, portanto, precisaremos calcular o valor de 'd'. Ou seja, d > 0 no Modelo ARIMA.

Então vamos fazer uma checagem. Vamos aplicar a diferenciação duas vezes a nossa série e comparar os gráficos ACF.

A função np.diff() aplica a diferenciação.


```python
# Área de Plotagem
fig, axes = plt.subplots(3, 2, sharex = True)

# Série Original
axes[0, 0].plot(df_treino['Close'].values); axes[0, 0].set_title('Série Original')
plot_acf(df_treino['Close'].values, lags = 150, ax = axes[0, 1])

# Diferenciação de Primeira Ordem
axes[1, 0].plot(np.diff(df_treino['Close'].values)); axes[1, 0].set_title('Diferenciação de Primeira Ordem')
plot_acf(np.diff(df_treino['Close'].values), lags = 150, ax = axes[1, 1])

# Diferenciação de Segunda Ordem
axes[2, 0].plot(np.diff(np.diff(df_treino['Close'].values))); axes[2, 0].set_title('Diferenciação de Segunda Ordem')
plot_acf(np.diff(np.diff(df_treino['Close'].values)), lags = 150, ax = axes[2, 1])

plt.show()
```


    
![png](assets/output_153_0.png)
    


Fica claro que a Diferenciação distribuiu melhor a série. Ou seja, o valor d = 1 ou d = 2 parecem ser boas opções para o Modelo ARIMA.

Vamos testar utilizando a função ndiffs:

https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.ndiffs.html


```python
# Teste ADF
print(ndiffs(df_valid['Close'], test = 'adf'))
print(ndiffs(df_treino['Close'], test = 'adf'))
```

    2
    0
    


```python
# Teste KPSS 
print(ndiffs(df_treino['Close'], test = 'kpss'))
print(ndiffs(df_treino['Close'], test = 'kpss'))
```

    1
    1
    

O Teste ADF indicou d = 2 para o conjunto de validação e d = 0 para o conjunto de treino enquanto que o Teste KPSS indicou d = 1 para ambos os conjuntos. Vamos escolher d = 1.

Já temos o I de ARIMA, o parâmetro d. Agora vamos encontrar o termo AR, com o parâmetro p.

**<h5 id="id-6.6.4">6.6.4) Determinando o Valor do Parâmetro p para o Modelo ARIMA</h5>**

A próxima etapa é identificar se o modelo precisa de termos AR. Você pode descobrir o número necessário de termos AR, inspecionando o gráfico PACF (Partial Autocorrelation). Mas o que é PACF?

A autocorrelação parcial pode ser imaginada como a correlação entre a série e seu atraso, após excluir as contribuições dos atrasos intermediários. Portanto, o PACF meio que transmite a correlação pura entre um atraso e a série. Dessa forma, você saberá se esse atraso é necessário no termo AR ou não.

Qualquer autocorrelação em uma série estacionarizada pode ser retificada adicionando termos AR suficientes. Portanto, inicialmente consideramos a ordem do termo AR igual a tantas defasagens que ultrapassam o limite de significância no gráfico PACF.


```python
# Gráfico PACF
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(np.diff(df_treino['Close'])); axes[0].set_title('Diferenciação de Primeira Ordem')
axes[1].set(ylim = (0,5))
plot_pacf(np.diff(df_treino['Close']), lags = 150, ax = axes[1])
plt.show()
```


    
![png](assets/output_159_0.png)
    



```python
# Autocorrelation Plot
plt.figure(figsize = [20,5]) 
autocorrelation_plot(df_treino['Close'])
plt.show()
```


    
![png](assets/output_160_0.png)
    


Você pode observar que o atraso (lag) 1 é bastante significativo, pois está bem acima da linha de significância. O atraso 2 também é significativo, conseguindo ultrapassar o limite de significância. Mas vou ser conservador e definir o valor do parâmetro p igual a 1. Já temos o termo AR. Falta um. 

**<h5 id="id-6.6.5">6.6.5) Determinando o Valor do Parâmetro q para o Modelo ARIMA</h5>**

Assim como observamos o gráfico PACF para o número de termos AR, você pode observar para o gráfico ACF para o número de termos MA. Um termo MA é tecnicamente o erro da previsão atrasada.

O ACF informa quantos termos MA são necessários para remover qualquer autocorrelação na série estacionarizada.

Vamos ver o gráfico de autocorrelação das séries diferenciadas.


```python
# Gráfico ACF
fig, axes = plt.subplots(1, 2, sharex = True)
axes[0].plot(np.diff(df_treino['Close'])); axes[0].set_title('Diferenciação de Primeira Ordem')
axes[1].set(ylim = (0,1.2))
plot_acf(np.diff(df_treino['Close']), ax = axes[1])
plt.show()
```


    
![png](assets/output_163_0.png)
    


O gráfico de autocorrelação indica que temos pelo menos um valor acima do limite de 0.2. Ou seja, q = 1 é o mínimo que deveríamos testar, embora o q = 2 seja uma opção. Você pode testar as duas opções se desejar, mas eu vou escolher q = 1.

> `Já temos os 3 parâmetros para o Modelo ARIMA (p, d, q) - order(1, 1, 1).`


```python
# Cria o Modelo ARIMA

# Definimos:

# p = 2
# d = 1
# q = 0

# Aqui o valor q é zero, pois é apenas o modelo AR. Na sequência eu explico porque.

# Modelo
modelo_AR = ARIMA(df_treino['Close'], order = (1, 1, 1))

# Treinamento
modelo_v2 = modelo_AR.fit(disp = -1) 

# Forecast
# O parâmetro alfa representa o intervalo de confiança, nesse caso, 95%
fc, se, conf = modelo_v2.forecast(len(df_valid), alpha = 0.05)
```


```python
df_valid['ARIMA V2'] = fc

df_limites = pd.DataFrame()
df_limites['Limite Inferior'] = conf[:, 0]
df_limites['Limite Superior'] = conf[:, 1]
df_limites.index = df_valid.index


df_valid['ARIMA V2'] = df_valid['ARIMA V2'].apply(lambda x: inv_boxcox(x, lambda_value))
df_limites['Limite Inferior'] = df_limites['Limite Inferior'].apply(lambda x: inv_boxcox(x, lambda_value))
df_limites['Limite Superior'] = df_limites['Limite Superior'].apply(lambda x: inv_boxcox(x, lambda_value))
```


```python
exibirResultadosComMargem(df_treino, df_valid, df_limites, 'ARIMA V2')
```

    O Resultado com a Métrica RMSE foi de: 1.8667943725641774
    



<h3 id="id-6.7">6.7) Modelo SARIMA</h3>

**<h5 id="id-6.7.1">6.7.1) Seasonal Autoregressive Integrated Moving-Average (SARIMA)</h5>**


A Média Móvel Integrada Autoregressiva Sazonal, SARIMA ou ARIMA Sazonal, é uma extensão do ARIMA que suporta explicitamente dados de séries temporais univariadas com um componente sazonal.

Esse modelo adiciona três novos hiperparâmetros para especificar a regressão automática (AR), a diferenciação (I) e a média móvel (MA) para o componente sazonal da série, além de um parâmetro adicional para o período da sazonalidade.

**<h5 id="id-6.7.2">6.7.2) Elementos de Tendência</h5>**

No modelo SARIMA existem três elementos de tendência que requerem configuração. Eles são iguais ao modelo ARIMA, especificamente:

- p: Ordem de regressão automática da tendência.
- d: Ordem de diferenciação da tendência.
- q: Ordem média móvel de tendência.

**<h5 id="id-6.7.3">6.7.3) Elementos de Sazonalidade</h5>**

E temos mais quatro elementos sazonais que não fazem parte do ARIMA e que devem ser configurados no modelo SARIMA. Eles são:

- P: Ordem autoregressiva sazonal.
- D: Ordem da diferença sazonal.
- Q: Ordem da média móvel sazonal.
- m: O número de etapas de tempo para um único período sazonal. Por exemplo, um S de 12 para dados mensais sugere um ciclo sazonal anual.

**<h5 id="id-6.7.4">6.7.4) Notação SARIMA</h5>**
SARIMA(p,d,q)(P,D,Q,m)

********* ATENÇÃO *********

Fique sempre atento às letras maiúsculas e minúsculas, pois isso faz toda diferença na interpretação dos parâmetros de ordem do modelo.

Criaremos algumas versões de modelo SARIMA a partir desta aula, para nosso problema de previsão de vendas, usando diferentes estratégias de Grid Search para busca dos valores ideais dos parâmetros de ordem.

O pacote pmdarima será útil em nosso trabalho: https://alkaline-ml.com/pmdarima/index.html

--- 
Até agora, restringimos nossa atenção aos dados não sazonais e aos modelos ARIMA não sazonais. No entanto, os modelos ARIMA também são capazes de modelar uma ampla variedade de dados sazonais.

A **Média Móvel Integrada Autoregressiva (ARIMA)** é um método de previsão para dados univariados de séries temporais.

Como o próprio nome sugere, ele suporta elementos médios autoregressivos e móveis. O elemento integrado refere-se à diferenciação, permitindo que o método suporte dados de séries temporais com uma tendência.

Um problema com o ARIMA é que ele não suporta dados sazonais, que é uma série temporal com um ciclo de repetição.

O ARIMA espera dados que não sejam sazonais ou que o componente sazonal seja removido, por exemplo, ajustado sazonalmente por métodos como diferenciação sazonal.

A **Média Móvel Integrada Autoregressiva Sazonal, SARIMA ou ARIMA Sazonal**, é uma extensão do ARIMA que suporta explicitamente dados de séries temporais univariadas com um componente sazonal.

Ele adiciona três novos hiperparâmetros para especificar a regressão automática (AR), a diferenciação (I) e a média móvel (MA) para o componente sazonal da série, além de um parâmetro adicional para o período da sazonalidade.

Um modelo ARIMA sazonal é formado pela inclusão de termos sazonais adicionais no ARIMA. A parte sazonal do modelo consiste em termos muito semelhantes aos componentes não sazonais do modelo, mas envolvem turnos alternados do período sazonal.

Um modelo ARIMA Sazonal é formado pela inclusão de termos sazonais adicionais nos modelos ARIMA que vimos até agora. Ou seja:

- Modelo ARIMA não sazonal = ARIMA(p, d, q)

- Modelo ARIMA sazonal = SARIMA(p,d,q)(P,D,Q,m)

Um modelo de média móvel integrada autoregressiva sazonal (SARIMA) é um passo diferente de um modelo ARIMA baseado no conceito de tendências sazonais. 

Em muitos dados de séries temporais, efeitos sazonais frequentes entram em cena. Tomemos, por exemplo, a temperatura média medida em um local com quatro estações. Haverá um efeito sazonal anualmente, e a temperatura nesta estação em particular definitivamente terá uma forte correlação com a temperatura medida no ano passado na mesma estação.

Considere o modelo SARIMA abaixo:

**<h5 id="id-6.7.5">6.7.5) Parâmetros SARIMA(3,1,0)(1,1,0)15</h5>**

O parâmetro m influencia os parâmetros P, D e Q. Por exemplo, um m de 12 para dados mensais sugere um ciclo sazonal quinzenal.

O parâmetro P = 1 usaria a primeira observação sazonalmente deslocada no modelo, ou seja, t-(m * 1) ou t-15.

O parâmetro P = 2, usaria as duas últimas observações de compensação sazonal t-(m * 1), t-(m * 2).

Da mesma forma, um D de 1 calcularia uma diferença sazonal de primeira ordem e um Q = 1 usaria erros de primeira ordem no modelo (por exemplo, média móvel).

Um modelo ARIMA sazonal usa diferenciação em um atraso igual ao número de seasons para remover efeitos sazonais aditivos. Assim como na diferenciação do atraso 1 para remover uma tendência, a diferenciação do atraso introduz um termo médio móvel. O modelo ARIMA sazonal inclui termos médios autoregressivos e móveis em lag s.

**<h5 id="id-6.7.6">6.7.6) Grid Search Método 1 - Stepwise Search</h5>**

Usando um Modelo Auto-Arima para retornar os melhores parâmetros de ordem da série, para o menor valor possível da Estatística AIC.

Fazer uma análise manual completa de séries temporais pode ser uma tarefa tediosa, especialmente quando você tem muitos conjuntos de dados para analisar. É preferível automatizar a tarefa de seleção de modelo com a pesquisa em grade (Grid Search). Para o SARIMA, como temos muitos parâmetros, a pesquisa em grade pode levar horas para ser concluída em um conjunto de dados se definirmos o limite de cada parâmetro muito alto. Definir limites muito altos também tornará seu modelo muito complexo e superestimará os dados de treinamento.

Para evitar o longo tempo de execução e o problema de sobreajuste (overfitting), aplicamos o que é conhecido como princípio de parcimônia, onde criamos uma combinação de todos os parâmetros tais que p + d + q + P + D + Q ≤ 6. Outra abordagem é definir cada parâmetro como 0 ou 1 ou 2 e fazer a pesquisa na grade usando o AIC em cada combinação. 

Usaremos a segunda opção, chamada Grid Search Stepwise. Vou definir limites pequenos para os hiperparâmetros, mas você pode testar outros valores se desejar.


```python
# Buscando pela ordem ideal para o modelo
# A função pm.auto_arima aplica o Grid Search e retorna o melhor modelo
modelo_v3 = pm.auto_arima(df_treino['Close'],
                          seasonal = True, 
                          m = 15,
                          d = 0, 
                          D = 1, 
                          max_p = 2, 
                          max_q = 2,
                          trace = True,
                          error_action = 'ignore',
                          suppress_warnings = True) 
```

    Performing stepwise search to minimize aic
     ARIMA(2,0,2)(1,1,1)[15] intercept   : AIC=inf, Time=11.81 sec
     ARIMA(0,0,0)(0,1,0)[15] intercept   : AIC=1930.424, Time=0.35 sec
     ARIMA(1,0,0)(1,1,0)[15] intercept   : AIC=-1846.035, Time=2.89 sec
     ARIMA(0,0,1)(0,1,1)[15] intercept   : AIC=411.001, Time=2.22 sec
     ARIMA(0,0,0)(0,1,0)[15]             : AIC=1961.278, Time=0.14 sec
     ARIMA(1,0,0)(0,1,0)[15] intercept   : AIC=-1409.566, Time=0.81 sec
     ARIMA(1,0,0)(2,1,0)[15] intercept   : AIC=-2028.007, Time=15.06 sec
     ARIMA(1,0,0)(2,1,1)[15] intercept   : AIC=inf, Time=18.24 sec
     ARIMA(1,0,0)(1,1,1)[15] intercept   : AIC=inf, Time=5.78 sec
     ARIMA(0,0,0)(2,1,0)[15] intercept   : AIC=1915.954, Time=4.61 sec
     ARIMA(2,0,0)(2,1,0)[15] intercept   : AIC=-2032.188, Time=14.16 sec
     ARIMA(2,0,0)(1,1,0)[15] intercept   : AIC=-1847.390, Time=4.27 sec
     ARIMA(2,0,0)(2,1,1)[15] intercept   : AIC=inf, Time=28.92 sec
     ARIMA(2,0,0)(1,1,1)[15] intercept   : AIC=inf, Time=8.92 sec
     ARIMA(2,0,1)(2,1,0)[15] intercept   : AIC=-2030.062, Time=23.93 sec
     ARIMA(1,0,1)(2,1,0)[15] intercept   : AIC=-2031.636, Time=17.56 sec
     ARIMA(2,0,0)(2,1,0)[15]             : AIC=-2033.088, Time=6.55 sec
     ARIMA(2,0,0)(1,1,0)[15]             : AIC=-1848.413, Time=2.54 sec
     ARIMA(2,0,0)(2,1,1)[15]             : AIC=inf, Time=19.52 sec
     ARIMA(2,0,0)(1,1,1)[15]             : AIC=inf, Time=7.72 sec
     ARIMA(1,0,0)(2,1,0)[15]             : AIC=-2028.750, Time=3.80 sec
     ARIMA(2,0,1)(2,1,0)[15]             : AIC=-2031.761, Time=10.88 sec
     ARIMA(1,0,1)(2,1,0)[15]             : AIC=-2032.530, Time=7.05 sec
    
    Best model:  ARIMA(2,0,0)(2,1,0)[15]          
    Total fit time: 217.791 seconds
    


```python
# Print do sumário do melhor modelo encontrado
print(modelo_v1.summary())
```

                                 ARIMA Model Results                              
    ==============================================================================
    Dep. Variable:                D.Close   No. Observations:                 1570
    Model:                 ARIMA(2, 1, 0)   Log Likelihood                1274.959
    Method:                       css-mle   S.D. of innovations              0.107
    Date:                Tue, 23 Aug 2022   AIC                          -2541.918
    Time:                        09:23:03   BIC                          -2520.483
    Sample:                             1   HQIC                         -2533.951
                                                                                  
    =================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    const             0.0040      0.003      1.555      0.120      -0.001       0.009
    ar.L1.D.Close    -0.0577      0.025     -2.286      0.022      -0.107      -0.008
    ar.L2.D.Close     0.0138      0.025      0.547      0.584      -0.036       0.063
                                        Roots                                    
    =============================================================================
                      Real          Imaginary           Modulus         Frequency
    -----------------------------------------------------------------------------
    AR.1           -6.6758           +0.0000j            6.6758            0.5000
    AR.2           10.8566           +0.0000j           10.8566            0.0000
    -----------------------------------------------------------------------------
    

Vamos então usar os valores encontrados pelo Grid Search e treinar um modelo SARIMA.

A implementação no Statsmodels é chamada SARIMAX em vez de SARIMA e a adição de "X" ao nome do método significa que a implementação também suporta variáveis exógenas.

Essas são variáveis de séries temporais paralelas que não são modeladas diretamente pelos processos AR, I ou MA, mas são disponibilizadas como entrada ponderada para o modelo.

Variáveis exógenas são opcionais e podem ser especificadas através do argumento “exog”.

https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html


```python
# Cria o Modelo SARIMA
modelo_sarima_v1 = sm.tsa.statespace.SARIMAX(df_treino['Close'],
                                                order = (2, 0, 0),
                                                seasonal_order = (2, 1, 0, 15),
                                                enforce_stationarity = False,
                                                enforce_invertibility = False)

# Treinamento (Fit) do modelo
modelo_sarima_v1_fit = modelo_sarima_v1.fit()

# Sumário do modelo
print(modelo_sarima_v1_fit.summary())
```

                                         SARIMAX Results                                      
    ==========================================================================================
    Dep. Variable:                              Close   No. Observations:                 1571
    Model:             SARIMAX(2, 0, 0)x(2, 1, 0, 15)   Log Likelihood                1007.182
    Date:                            Tue, 23 Aug 2022   AIC                          -2004.364
    Time:                                    09:23:56   BIC                          -1977.718
    Sample:                                         0   HQIC                         -1994.445
                                               - 1571                                         
    Covariance Type:                              opg                                         
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    ar.L1          0.9027      0.017     53.382      0.000       0.870       0.936
    ar.L2          0.0722      0.017      4.184      0.000       0.038       0.106
    ar.S.L15      -0.6793      0.015    -43.990      0.000      -0.710      -0.649
    ar.S.L30      -0.3410      0.015    -22.257      0.000      -0.371      -0.311
    sigma2         0.0156      0.000     63.156      0.000       0.015       0.016
    ===================================================================================
    Ljung-Box (L1) (Q):                   0.02   Jarque-Bera (JB):             12806.22
    Prob(Q):                              0.88   Prob(JB):                         0.00
    Heteroskedasticity (H):               2.17   Skew:                            -1.39
    Prob(H) (two-sided):                  0.00   Kurtosis:                        16.93
    ===================================================================================
    
    Warnings:
    [1] Covariance matrix calculated using the outer product of gradients (complex-step).
    


```python
# Vamos fazer previsões um passo a frente
#sarima_predict_1 = modelo_sarima_v1_fit.get_prediction(dynamic = False)

fc = modelo_sarima_v1_fit.forecast(len(df_valid))
```


```python
df_valid['SARIMA'] = fc.values

df_valid['SARIMA'] = df_valid['SARIMA'].apply(lambda x: inv_boxcox(x, lambda_value))

exibirResultados(df_treino, df_valid, 'SARIMA')
```

    O Resultado com a Métrica RMSE foi de: 1.9937737721864746
    



<h2 id="id-7">7) FORECASTING</h2>

<h3 id="id-7.1">7.1) Utilizando o modelo SARIMA para prever os próximos 6 meses</h3>

Pela métrica de avaliação podemos ver que o melhor modelo dentre todos foi os modelos SARIMA. Portanto, iremos utilizar este modelo para realizar as previsões para os próximos seis meses.


```python
df['CloseBoxCox'], lambda_value = boxcox(df['Close'])

# Cria o Modelo SARIMA
modelo_final = sm.tsa.statespace.SARIMAX(df['CloseBoxCox'],
                                                order = (2, 0, 0),
                                                seasonal_order = (2, 1, 0, 60),
                                                enforce_stationarity = False,
                                                enforce_invertibility = False)

# Treinamento (Fit) do modelo
modelo_final_fit = modelo_final.fit()

# Sumário do modelo
print(modelo_final_fit.summary())

fc = modelo_final_fit.forecast(180, alpha = 0.05)
```

                                         SARIMAX Results                                      
    ==========================================================================================
    Dep. Variable:                        CloseBoxCox   No. Observations:                 1637
    Model:             SARIMAX(2, 0, 0)x(2, 1, 0, 60)   Log Likelihood                 933.828
    Date:                            Tue, 23 Aug 2022   AIC                          -1857.656
    Time:                                    09:25:59   BIC                          -1831.242
    Sample:                                         0   HQIC                         -1847.801
                                               - 1637                                         
    Covariance Type:                              opg                                         
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    ar.L1          0.9381      0.017     53.751      0.000       0.904       0.972
    ar.L2          0.0530      0.018      2.980      0.003       0.018       0.088
    ar.S.L60      -0.6600      0.017    -39.840      0.000      -0.693      -0.628
    ar.S.L120     -0.3344      0.017    -19.424      0.000      -0.368      -0.301
    sigma2         0.0162      0.000     58.056      0.000       0.016       0.017
    ===================================================================================
    Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):              7567.39
    Prob(Q):                              0.97   Prob(JB):                         0.00
    Heteroskedasticity (H):               1.82   Skew:                            -1.19
    Prob(H) (two-sided):                  0.00   Kurtosis:                        13.92
    ===================================================================================
    
    Warnings:
    [1] Covariance matrix calculated using the outer product of gradients (complex-step).
    


```python
#Essa função gera o dataframe com as datas de acordo com a quantidade dos dados.

def geraDatas(df, dados, dataInicial):
    
    quantidade = len(dados) + 1
    freq = 'B' #Frequência B significa: Pegue todos os dias ignorando finais de semana.
    strftime = '%Y-%m-%d' #Formato que eu quero (Year-Month-Day)

    datas = pd.date_range(start=dataInicial, periods=quantidade, freq=freq)[1:]
    datas = pd.to_datetime(datas.strftime(strftime))

    df = pd.DataFrame(dados)
    df['Date'] = datas

    df.columns = ['Valores Previstos', 'Date']
    df = df[['Date', 'Valores Previstos']]

    return df
```


```python
df_preds = pd.DataFrame()

dt_final = df.iloc[-1].Date + timedelta(days=1)
df_preds = geraDatas(df_preds, fc, dataInicial=dt_final)

#Para cada valor previsto, aplique a função inv_boxcox.
df_preds['Valores Previstos'] = df_preds['Valores Previstos'].apply(lambda x: inv_boxcox(x, lambda_value))
```


```python
fig = go.Figure()

fig.add_traces(go.Line(x=df['Date'], y=df['Close'], name='Dados Reais'))
fig.add_traces(go.Line(x=df_preds['Date'], y=df_preds['Valores Previstos'], name='Valores Previstos'))


fig.update_layout(
        title='<span>Previsões para os próximos 6 meses com o modelo SARIMA</span>', 
        autosize=False,
        width=1200,
        height=500,
        xaxis=dict(title=f'<span>Tempo</span>'),
        yaxis=dict(title=f'<span>Valores</span>')
    )

fig.show()
```



---
<h2 id="id-8">8) CONSIDERAÇÕES SOBRE O PROJETO</h2>

<h3 id="id-8.1">8.1) Considerações</h3>

No decorrer deste projeto foram apresentados várias técnicas de análise exploratória, análise estatística e descritiva dos dados. Em termos de séries temporais, utilizamos a principais técnicas e conceitos para transformação nos dados. Técnicas estas que são as principais utilizadas atualmente nos projetos envolvendos séries temporais.

Para o modelo Preditivo, o meu principal foco foi realizar um estudo detalhado e completo sobre os modelos ARIMA, um dos principais algoritmos para realizar a modelagem preditiva em séries temporais. Um detalhe dos modelos arima, especificamente do modelo SARIMA é o parâmetro `Periodicidade` que faz os calculos baseados no período definido. Este é um parâmetro bastante relevante para garantir uma boa precisão do modelo, mas vale ressaltar que, quanto maior for a periodicidade escolhida, maior será o custo em realizar previsão. Portanto, cabe ao analista definir um bom balanço entre um `Custo` x `Benefício`.

O projeto abordou um tema que é extenso e exige meses (até anos) de estudo, que é o assunto de Análise de Séries Temporais. Eu quis compilar o máximo de conhecimento que eu tenho até aqui nesse tema. E foi de grande valia para mim, e pode ser de grande ajuda para quem estiver interessado sobre esse assunto. 

Como trabalhos futuros, pode-se realizar uma modelagem preditiva utilizando as técnicas de Redes Neurais Recorrentes, conbsiderado atualmente o estado da arte  em modelagem preditiva de Séries Temporais. Eu decidi não inserir esta técnica porque não foi o meu foco no desenvolvimento deste projeto.



---

<h3 id="id-8.2">8.2) Streamlit</h3>

Eu desenvolvi uma aplicação completa utilizando o Streamlit. Lá eu inseri todas as técnicas que trouxeram os melhores resultados neste projeto. Na aplicação desenvolvida você pode escolher a ação desejada `['AAPL', 'AMZN', 'NVDA']`, dentre centenas de empresas listadas na bolsa de valores e realizar a sua própria análise de ações.

Além disso, você pode escolher o período no qual você deseja realizar as análises. A data inicial, a data final, o tipo de agrupamento (`Dias`, `Meses`, `Anos`) e o método utilizado para agrupar os dados (`Somatório`, `Média` ou `Mediana`).

Por fim, é possível realizar a previsão dos ativos para os próximos períodos. Em dias, meses e anos. Você escolhe a quantidade de períodos e também a quantidade de periodicidade, que eu citei acima.

> O link para a aplicação está aqui: https://app-stock-exchange.herokuapp.com

---

<h3 id="id-8.3">8.3) Referências</h3>

* [1] Data Science Academy, 2021. *Análise Estatística e Modelagem Preditiva de Séries Temporais*. Disponível somente para quem comprou algum outro curso pago da [plataforma](datascienceacademy.com.br)

* [2] Equipe Toro Investimentos, 2022. *O que são ações? Entenda as ordinárias e preferenciais e como comprar!*. Disponível em:<[toroinvestimentos.com](https://blog.toroinvestimentos.com.br/o-que-sao-acoes-ordinaria-preferencial)>

* [3] Leite, Vitor, 2021. *O que são ações e o que significa “investir na Bolsa”?*. Disponível em:<[nubank.com](https://blog.nubank.com.br/o-que-sao-acoes/)>

* [4] Myers, D.E., 1989. *To be or not to be . . . stationary?* That is the question. Disponível em:<[arizona.edu](http://www.u.arizona.edu/~donaldm/homepage/my_papers/MathGeology_21_1989_347-363.pdf)>


* [5] Reis, Tiago, 2017. *O que são ações Ordinárias, Preferenciais e Units?*. Disponível em:<[suno.com](https://www.suno.com.br/artigos/o-que-sao-acoes-ordinarias-preferenciais-e-units/)>
	
* [6] Reis, Tiago, 2020. *O que são Units? Entenda como funciona esse tipo de ação*. Disponível em:<[suno.com](https://www.suno.com.br/artigos/units/#:~:text=As%20Units%20são%20um%20tipo%20de%20ativo%2C%20negociadas%20no%20mercado,PN%20e%20bônus%20de%20subscrição.)>

* [7] Smigel, Leo, 2022. *What Is Stationarity? A Visual Guide*. Disponível em:<[analyzingalpha](https://analyzingalpha.com/stationarity)>

* [8] Pérez, Fernando, 2022. *Análise de Séries Temporais. Capítulo III. Modelos ARIMA*. Disponível em:<[ufpr.br](http://leg.ufpr.br/~lucambio/STemporais/STemporaisIII.html)>

---

<h3 id="id-8.4">8.4) Agradecimentos</h3>

Esse foi um projeto extenso, para quem chegou até aqui, espero que tenha ajudado a entender mais sobre as Séries Temporais e modelagem preditiva utilizando os modelos ARIMA e SARIMA.

Qualquer dúvida, sugestão, apotamento ou crítica é bem vinda. Pode entrar em contato em: `krupck@outlook.com`

Atenciosamente,

<br/><br/>
**Henrique Krupck**

---

# FIM
