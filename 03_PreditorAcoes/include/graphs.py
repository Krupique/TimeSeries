import pandas as pd
import numpy as np

# Visualização dos dados
import matplotlib.pyplot as plt
import matplotlib as m
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff


def exibirTimeSeries(list_df, list_tickers, x, y, title = 'Title Default', width = 1000, height = 400, xlabel = 'xlabel', ylabel = 'ylabel'):
    fig = go.Figure()
    
    for i in range(len(list_df)):

        df = list_df[i]
        fig.add_traces(go.Line(x=df[x], y=df[y], name=list_tickers[i]))

    fig.update_layout(
        title=f'<span>{title}</span>', 
        autosize=False,
        width=width,
        height=height,
        xaxis=dict(title=f'<span>{xlabel}</span>'),
        yaxis=dict(title=f'<span>{ylabel}</span>')
    )

    return fig
