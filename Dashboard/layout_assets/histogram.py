#--------------------- Packages
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import plotly.graph_objects as go
#--------------------- Boxpot
def histogram_asset(df_1, df_2, df_3, df_4, name_1, name_2, name_3, name_4):
    """Function to create a four subplots with distributions using four different dataframes"""
    fig = make_subplots(
        rows=2, cols=2,
        shared_yaxes=True, shared_xaxes=False,
        horizontal_spacing=0.04, vertical_spacing=0.18,
        subplot_titles=(name_1, name_2, name_3, name_4))

    # iPhone 11
    fig.add_trace(
        go.Histogram(
            x=np.array(df_1['price']),
            name=name_1, showlegend=False,
            marker=dict(color='Orange')),
        row=1, col=1)

    # iPhone SE
    fig.add_trace(
        go.Histogram(
            x=np.array(df_2['price']),
            name=name_2, showlegend=False,
            marker=dict(color='Magenta')),
        row=1, col=2)

    # Note 10
    fig.add_trace(
        go.Histogram(
            x=np.array(df_3['price']),
            name=name_3, showlegend=False,
            marker=dict(color='Green')),
        row=2, col=1)

    # S20 Ultra
    fig.add_trace(
        go.Histogram(
            x=np.array(df_4['price']),
            name=name_4, showlegend=False,
            marker=dict(color='Gold')),
        row=2, col=2)

    # Axes Parameters
    fig.update_xaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', automargin=True,
        ticks="outside", tickwidth=2,
        tickcolor='black', ticklen=12)

    fig.update_yaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', ticks="outside",
        tickwidth=2, tickcolor='black',
        ticklen=12, type="log", automargin=True)

    # Update Axes Titles
    fig.update_xaxes(
        row=2, col=1,
        title_text='Price ($)', title_font=dict(size=22))

    fig.update_xaxes(
        row=2, col=2,
        title_text='Price ($)', title_font=dict(size=22))

    fig.update_yaxes(
        row=1, col=1,
        title_text='Count', title_font=dict(size=22))

    fig.update_yaxes(
        row=2, col=1,
        title_text='Count', title_font=dict(size=22))
    
    # Create subplot titles
    for i in fig['layout']['annotations']:
        i['font'] = dict(size=22, color='#ff0000')

    # Layout parameters
    fig.update_layout(
        height=650, width=850,
        plot_bgcolor="#f7f7f7", paper_bgcolor="#f7f7f7",
        title_text="<b>Distribution of Popular Phone Auctions</b>", title_font=dict(size=28),
        title=dict(
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'),
        font=dict(
            size=20,
            family="Courier New, monospace"
        ),
        hoverlabel=dict(
            font_size=22,
            font_family="Rockwell"
        )
    )

    return fig
