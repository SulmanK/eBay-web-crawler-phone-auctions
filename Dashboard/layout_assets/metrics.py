#--------------------- Packages
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import plotly.graph_objects as go
#--------------------- Boxpot
def metrics_asset(df_1, df_2, df_3, df_4, name_1, name_2, name_3, name_4):
    """Function to create a four subplots with metrics using four different dataframes"""
    fig = make_subplots(
        rows=2, cols=2,
        shared_yaxes=True, shared_xaxes=True,
        horizontal_spacing=0.04, vertical_spacing=0.18,
        subplot_titles=(name_1, name_2, name_3, name_4))

    # iPhone 11
    fig.add_trace(
        go.Bar(
            x=['Min'], y=np.array(df_1['price'].min()),
            name=name_1, showlegend=False,
            marker=dict(color='Red')),
        row=1, col=1)

    fig.add_trace(
        go.Bar(
            x=['Mean'], y=np.array(df_1['price'].mean()),
            name=name_1, showlegend=False,
            marker=dict(color='Teal')),
        row=1, col=1)

    fig.add_trace(
        go.Bar(
            x=['Median'], y=np.array(df_1['price'].median()),
            name=name_1, showlegend=False,
            marker=dict(color='Olive')),
        row=1, col=1)

    fig.add_trace(
        go.Bar(
            x=['Max'], y=np.array(df_1['price'].max()),
            name=name_1, showlegend=False,
            marker=dict(color='Purple')),
        row=1, col=1)

    # iPhone SE
    fig.add_trace(
        go.Bar(
            x=['Min'], y=np.array(df_2['price'].min()),
            name=name_2, showlegend=False,
            marker=dict(color='Red')),
        row=1, col=2)

    fig.add_trace(
        go.Bar(
            x=['Mean'], y=np.array(df_2['price'].mean()),
            name=name_2, showlegend=False,
            marker=dict(color='Teal')),
        row=1, col=2)

    fig.add_trace(
        go.Bar(
            x=['Median'], y=np.array(df_2['price'].median()),
            name=name_2, showlegend=False,
            marker=dict(color='Olive')),
        row=1, col=2)

    fig.add_trace(
        go.Bar(x=['Max'], y=np.array(df_2['price'].max()),
               name=name_2, showlegend=False,
               marker=dict(color='Purple')),
        row=1, col=2)

    # Note 10
    fig.add_trace(
        go.Bar(
            x=['Min'], y=np.array(df_3['price'].min()),
            name=name_3, showlegend=False,
            marker=dict(color='Red')),
        row=2, col=1)

    fig.add_trace(
        go.Bar(
            x=['Mean'], y=np.array(df_3['price'].mean()),
            name=name_3, showlegend=False,
            marker=dict(color='Teal')),
        row=2, col=1)

    fig.add_trace(
        go.Bar(
            x=['Median'], y=np.array(df_3['price'].median()),
            name=name_3, showlegend=False,
            marker=dict(color='Olive')),
        row=2, col=1)

    fig.add_trace(
        go.Bar(
            x=['Max'], y=np.array(df_3['price'].max()),
            name=name_3, showlegend=False,
            marker=dict(color='Purple')),
        row=2, col=1)

    # S20 Ultra
    fig.add_trace(
        go.Bar(
            x=['Min'], y=np.array(df_4['price'].min()),
            name=name_4, showlegend=False,
            marker=dict(color='Red')),
        row=2, col=2)

    fig.add_trace(
        go.Bar(
            x=['Mean'], y=np.array(df_4['price'].mean()),
            name=name_4, showlegend=False,
            marker=dict(color='Teal')),
        row=2, col=2)

    fig.add_trace(
        go.Bar(
            x=['Median'], y=np.array(df_4['price'].median()),
            name=name_4, showlegend=False,
            marker=dict(color='Olive')),
        row=2, col=2)

    fig.add_trace(
        go.Bar(
            x=['Max'], y=np.array(df_4['price'].max()),
            name=name_4, showlegend=False,
            marker=dict(color='Purple')),
        row=2, col=2)

    # Axes Parameters
    fig.update_xaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', automargin=True,
        ticks="outside", tickwidth=2,
        tickcolor='black', ticklen=12,
        showgrid=False)

    fig.update_yaxes(
        linewidth=1, linecolor='black',
        gridcolor='LightPink', ticks="outside",
        tickwidth=2, tickcolor='black',
        ticklen=12, type="log", automargin=True)

    # Update Y-axis titles
    fig.update_xaxes(
        row=2, col=1,
        title_text='Metric', title_font=dict(size=22))

    fig.update_xaxes(
        row=2, col=2,
        title_text='Metric', title_font=dict(size=22))

    # Update Y-axis titles
    fig.update_yaxes(
        row=1, col=1,
        title_text='Price ($)', title_font=dict(size=22))

    fig.update_yaxes(
        row=2, col=1,
        title_text='Price ($)', title_font=dict(size=22))

    # Create subplot axes titles
    for i in fig['layout']['annotations']:
        i['font'] = dict(size=22, color='#ff0000')

    # Layout parameters
    fig.update_layout(
        height=650, width=850,
        plot_bgcolor="#f7f7f7", paper_bgcolor="#f7f7f7",
        title_text="<b>Metrics of Popular Phone Auctions</b>", title_font=dict(size=28),
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
