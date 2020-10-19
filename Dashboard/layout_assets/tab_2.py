#--------------------- Packages
from app import app
from dash.dependencies import Input, Output, State
from layout_assets.boxplot import boxplot_asset
from layout_assets.datatable import datatable_asset
from layout_assets.histogram import histogram_asset
from layout_assets.metrics import metrics_asset
from layout_assets.moving_average_figure import moving_average_asset
from model.data_pull import df_ip11, df_ipse, df_sg10, df_sg20
from model.moving_average import moving_average_df
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

# Instantiate variables
df_ma_ip11 = moving_average_df(df_ip11)
df_ma_ipse = moving_average_df(df_ipse)
df_ma_sg10 = moving_average_df(df_sg10)
df_ma_sg20 = moving_average_df(df_sg20)


df_aa_ip11 = df_ip11[df_ip11['active_auction'] == 'YES']
df_aa_ipse = df_ipse[df_ipse['active_auction'] == 'YES']
df_aa_sg10 = df_sg10[df_sg10['active_auction'] == 'YES']
df_aa_sg20 = df_sg20[df_sg20['active_auction'] == 'YES']

# Instantiate figures
boxplot_auctions = boxplot_asset(
    df_1=df_ip11, df_2=df_ipse,
    df_3=df_sg10, df_4=df_sg20,
    name_1='iPhone 11', name_2='iPhone SE',
    name_3='Note 10', name_4='S20 Ultra')

metrics_auctions = metrics_asset(
    df_1=df_ip11, df_2=df_ipse,
    df_3=df_sg10, df_4=df_sg20,
    name_1='iPhone 11', name_2='iPhone SE',
    name_3='Note 10', name_4='S20 Ultra')

histogram_auctions = histogram_asset(
    df_1=df_ip11, df_2=df_ipse,
    df_3=df_sg10, df_4=df_sg20,
    name_1='iPhone 11', name_2='iPhone SE',
    name_3='Note 10', name_4='S20 Ultra')

moving_average_auctions = moving_average_asset(
    df_1=df_ma_ip11, df_2=df_ma_ipse,
    df_3=df_ma_sg10, df_4=df_ma_sg20,
    name_1='iPhone 11', name_2='iPhone SE',
    name_3='Note 10', name_4='S20 Ultra')


# --------------------- Tab 2
"""Second Tab of Plotly Dash Web Application"""
# game_list input for dropdown

# Tab 2
tab_2_layout = html.Div(
    [
        # Heading for game input and dropdown
        html.Div(
            [

                dcc.Markdown('## Visualizations'),

            ], style={"padding-left": "2rem"}
        ),

        # Heading for recommendations methods, dropdown, and button
        html.Div(
            [

                dcc.Graph(figure=boxplot_auctions)

            ], style={'width': '100%', 'display': 'flex',
                      'align-items': 'center', 'justify-content': 'center'}
        ),

        html.Div(
            [

                html.Div(
                    [

                        dcc.Graph(figure=metrics_auctions),

                    ], style={'display': 'inline-block', 'padding-left': '5rem'}
                ),

                html.Div(
                    [

                        dcc.Graph(figure=histogram_auctions),

                    ], style={'display': 'inline-block'}
                ),

                html.Div(
                    [

                        dcc.Graph(figure=moving_average_auctions),

                    ], style={'width': '100%', 'display': 'flex',
                              'align-items': 'center', 'justify-content': 'center'}
                ),

                html.Div(
                    [

                        dcc.Markdown('## Datatable'),

                    ], style={"padding-left": "2rem"}
                ),

                html.Div(
                    [

                        dcc.Markdown(
                            '#### Drag the slider to change the datatable:'),

                    ], style={"padding-left": "4rem"}
                ),

                # Slider has included=True by default
                html.Div([
                    dcc.Slider(
                        id='phone-slider',
                        min=0,
                        max=75,
                        step=None,
                        value=0,
                        marks={
                            0: {'label': 'iPhone 11', },
                            25: {'label': 'iPhone SE'},
                            50: {'label': 'Note 10'},
                            75: {'label': 'S20 Ultra'}
                        },
                    ),

                ], style={'padding-left': '14.2rem',
                          'padding-right': '10.2rem', 'padding-top': '2rem'}),



                html.Div(
                    [

                        dcc.Markdown(
                            '#### Drag the slider to set the threshold price:'),

                    ], style={"padding-left": "4rem", 'padding-top': '5rem'}
                ),

                # Slider has included=True by default
                html.Div([
                    dcc.Slider(
                        id='price-slider',
                        min=0,
                        max=2000,
                        step=10,
                        value=1000,
                        updatemode='drag',
                        marks={
                            0: {'label': '$0', },
                            500: {'label': '$500'},
                            1000: {'label': '$1000'},
                            1500: {'label': '$1500'},
                            2000: {'label': '$2000'}
                        },
                    ),

                ], style={'padding-left': '14.2rem',
                          'padding-right': '10.2rem', 'padding-top': '2rem'}),


                html.Div(id='updatemode-output-container', style={'padding-top': '3rem', 'fontSize': 30,
                                                                  'padding-left': '139rem', 'color': '#5e895e',
                                                                  'fontWeight': 'bold'}),

                html.Div([html.Div(id='datatable-with-slider', style={'fontWeight': 'bold'}),
                          ], style={"padding-top": "0rem"}),


            ]
        )

    ]
)


@app.callback(Output('updatemode-output-container', 'children'),
              [Input('price-slider', 'value')])
def display_value(value):
    return 'Threshold Price: $' + str(value)


# Callback Functions
"""Recommendation Results Callback - Datatable, Wordcloud, logo-recommendations, tf-idf bar distribution and wordcloud."""


@app.callback(
    Output('datatable-with-slider', 'children'),
    [Input('phone-slider', 'value'), Input('price-slider', 'value')])
def update_figure(phone_model, threshold_price):

    if phone_model == 0:
        div_datatable = datatable_asset(
            df=df_aa_ip11[df_aa_ip11['price'] <= threshold_price])

    elif phone_model == 25:
        div_datatable = datatable_asset(
            df=df_aa_ipse[df_aa_ipse['price'] <= threshold_price])

    elif phone_model == 50:
        div_datatable = datatable_asset(
            df=df_aa_sg10[df_aa_sg10['price'] <= threshold_price])

    elif phone_model == 75:
        div_datatable = datatable_asset(
            df=df_aa_sg20[df_aa_sg20['price'] <= threshold_price])

    return div_datatable
