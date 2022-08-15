import pandas as pd
import numpy as np

# Visualização dos dados
import matplotlib.pyplot as plt
import matplotlib as m
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff


def exibirGrafico(list_df, list_tickers, x, y, type, title = 'Title Default', width = 1000, height = 400, xlabel = 'xlabel', ylabel = 'ylabel'):
    fig = go.Figure()
    
    for i in range(len(list_df)):

        df = list_df[i]

        if type == 'bar':
            fig.add_traces(go.Bar(x=df[x], y=df[y], name=list_tickers[i]))
        elif type == 'line':
            fig.add_traces(go.Line(x=df[x], y=df[y], name=list_tickers[i]))
        elif type == 'box':
            fig.add_traces(go.Box(x=df[x], y=df[y], name=list_tickers[i]))
        elif type == 'histogram':
            fig.add_traces(go.Histogram(x=df[y], name=list_tickers[i]))


    fig.update_layout(
        title=f'<span>{title}</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title=f'<span>{xlabel}</span>'),
        yaxis=dict(title=f'<span>{ylabel}</span>'),
        margin=dict(l=10, r=10, t=35, b=0),
    )

    return fig


def exibirCanddleStick(df, x, name = 'ticket', title = 'Title Default', width = 1000, height = 400, xlabel = 'xlabel', ylabel = 'ylabel'):
    trace1 = {
        'x': df[x],
        'open': df['Open'],
        'close': df['Close'],
        'high': df['High'],
        'low': df['Low'],
        'type': 'candlestick',
        'name': name,
        'showlegend': False
    }

    data = [trace1]
    layout = go.Layout()

    fig = go.Figure(data = data, layout = layout)



    fig.update_layout(
        title=f'<span>{title}</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title=f'<span>{xlabel}</span>'),
        yaxis=dict(title=f'<span>{ylabel}</span>'),
        xaxis_rangeslider_visible=False,
        margin=dict(l=10, r=10, t=35, b=0)
    )

    return fig

def adicionarTrace(fig, df, x, y = 'Close', name='Default', color='#FF0'):

    fig.add_traces(go.Line(x=df[x], y=df[y], name=name, marker={'color': color}))

    return fig


def exibirGraficoSustentabilidade(x, y, width, height):
    fig = go.Figure()

    x_value_map ={
        'socialScore': 'Score Social',
        'governanceScore': 'Score Governamental',
        'environmentScore': 'Score Ambiental',
        'totalEsg': 'Score Total',
    }

    x = x.map(x_value_map)


    for i in range(len(x)):
        fig.add_traces(go.Bar(x = [x[i]], y = [y[i]], text=[y[i]], name=x[i]))


    fig.update_layout(
        title=f'<span>Indicadores de Sustentabilidade da Empresa</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title='<span>Indicadores</span>'),
        yaxis=dict(title='<span>Valores</span>'),
        xaxis_rangeslider_visible=False,
        margin=dict(l=10, r=10, t=35, b=0)
    )

    return fig

