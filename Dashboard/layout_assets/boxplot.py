#--------------------- Packages
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import plotly.graph_objects as go
#--------------------- Boxplot
def boxplot_asset(df_1, df_2, df_3, df_4, name_1, name_2, name_3, name_4):
    """Function to create a four boxplots using four different dataframes"""
    # Create subplot object
    fig = make_subplots(
        rows=1, cols=4,
        shared_yaxes=True, horizontal_spacing=0.05)

    # Add traces
    fig.add_trace(
        go.Box(
            x=df_1['model'], y=df_1['price'],
            name='name_1', showlegend=False),
        row=1, col=1)

    fig.add_trace(
        go.Box(
            x=df_2['model'], y=df_2['price'],
            name='name_2', showlegend=False),
        row=1, col=2)

    fig.add_trace(
        go.Box(
            x=df_3['model'], y=df_3['price'],
            name='name_3', showlegend=False),
        row=1, col=3)

    fig.add_trace(
        go.Box(
            x=df_4['model'], y=df_4['price'],
            name='name_4', showlegend=False),
        row=1, col=4)

    # Axes parameters
    fig.update_xaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', automargin=True,
        ticks="outside", tickwidth=2,
        tickcolor='black', ticklen=12,
        showgrid=False, title_font=dict(size=22))

    fig.update_yaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', ticks="outside",
        tickwidth=2, tickcolor='black',
        ticklen=12, type='log', automargin=True)

    # Title axes
    fig.update_yaxes(
        title='Price ($)', title_font=dict(size=22),
        row=1, col=1)

    # Layout
    fig.update_layout(
        height=450, width=1000,
        plot_bgcolor="#f7f7f7", paper_bgcolor="#f7f7f7",
        title=dict(
            y=0.9,
            x=0.5,
            xanchor='center',
            yanchor='top'),

        title_text="<b>Boxplot of Popular Phone Auctions</b>", title_font=dict(size=28),
        font=dict(
            size=22,
            family="Courier New, monospace"
        ),
        hoverlabel=dict(
            font_size=22,
            font_family="Rockwell"
        ))

    return fig
