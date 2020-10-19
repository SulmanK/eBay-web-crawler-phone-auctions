#--------------------- Packages
import numpy as np
import pandas as pd
import plotly.graph_objects as go
# --------------------- Moving Average figure
def moving_average_asset(
        df_1, df_2,
        df_3, df_4,
        name_1, name_2,
        name_3, name_4):
    "Function to plot a moving average figure"

    # Calculate moving average
    ma_df_1 = pd.Series(df_1['mean_price']).rolling(
        window=90, min_periods=1).mean()
    ma_df_2 = pd.Series(df_2['mean_price']).rolling(
        window=90, min_periods=1).mean()
    ma_df_3 = pd.Series(df_3['mean_price']).rolling(
        window=90, min_periods=1).mean()
    ma_df_4 = pd.Series(df_4['mean_price']).rolling(
        window=90, min_periods=1).mean()

    # Create plotly figure object
    fig = go.Figure()

    # iPhone 11
    fig.add_trace(
        go.Scatter(
            x=df_1['date'], y=ma_df_1,
            name=name_1, showlegend=False,
            marker=dict(color='Orange')),)

    # iPhone SE
    fig.add_trace(
        go.Scatter(
            x=df_2['date'], y=ma_df_2,
            name=name_2, showlegend=False,
            marker=dict(color='Magenta'),
            visible=False),)

    # Note 10
    fig.add_trace(
        go.Scatter(
            x=df_3['date'], y=ma_df_3,
            name=name_3, showlegend=False,
            marker=dict(color='Green'),
            visible=False),
    )

    # S20 Ultra
    fig.add_trace(
        go.Scatter(
            x=df_4['date'], y=ma_df_4,
            name=name_4, showlegend=False,
            marker=dict(color='Gold'),
            visible=False),
    )

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
        ticklen=12, automargin=True)

    # Update Axes Titles
    fig.update_xaxes(
        title_text='Date', title_font=dict(size=22), type="date",
        autorange=True)

    fig.update_yaxes(
        title_text='Moving Average ($)', title_font=dict(size=22))

    # Layout parameters
    fig.update_layout(
        xaxis_rangeslider=dict(
            visible=True),
        xaxis_tickformat='%b %d',
        height=650, width=1000,
        plot_bgcolor="#f7f7f7", paper_bgcolor="#f7f7f7",
        title_text="<b>Moving Average of iPhone 11 Auctions</b>",
        title_font=dict(size=28),
        title=dict(
            y=0.85,
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
        ),

    ),

    fig.update_layout(

        updatemenus=[

            dict(
                active=0,
                x=-0.1,
                xanchor='left',
                y=1.3,
                yanchor='top',
                bordercolor='#ffc7e2',
                font=dict(size=28, color='#000000'),
                buttons=list([
                    dict(label="<b>iPhone 11</b>",
                         method="update",
                         args=[
                             {"visible": [True, False, False, False]},
                             {"title": "<b>Moving Average of iPhone 11 Auctions</b>"}]),
                    dict(label="<b>iPhone SE</b>",
                         method="update",
                         args=[{"visible": [False, True, False, False]},
                               {"title": "<b>Moving Average of iPhone SE Auctions</b>"}]),
                    dict(label="<b>Note 10</b>",
                         method="update",
                         args=[{"visible": [False, False, True, False]},
                               {"title": "<b>Moving Average of Note 10 Auctions</b>",
                                }]),
                    dict(label="<b>S20 Ultra</b>",
                         method="update",
                         args=[{"visible": [False, False, False, True]},
                               {"title": "<b>Moving Average of S20 Ultra Auctions</b>",
                                }]),
                ]),
            )
        ]
    )

    return fig
