#--------------------- Packages
from app import app
from dash.dependencies import Input, Output
from layout_assets.boxplot import boxplot_asset
from layout_assets.histogram import histogram_asset
from layout_assets.metrics import metrics_asset
from layout_assets.tab_1 import tab_1_layout
from layout_assets.tab_2 import tab_2_layout
from model.data_pull import df_ip11, df_ipse, df_sg10, df_sg20
from model.moving_average import moving_average_df
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
# --------------------- Main Layout
"""Main Page of Web Application"""
# Style of Tabs
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'fontSize': '2.5rem'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ffc7e2',
    'color': 'white',
    'padding': '6px',
    'fontSize': '2.5rem',
}

# Layout
main_layout = html.Div(
    [
        html.Div(

            # Create Banner Layout (Title and Logos)
            [
                html.Div(
                    [

                        # Input Title of Dashboard, Include title and href link
                        html.H2(
                            id="banner-title",
                            children=[
                                html.A(
                                    "eBay: Monitoring Phone Auctions",
                                    href="https://github.com/SulmanK/eBay-web-crawler-phone-auctions",
                                    style={
                                        "text-decoration": "none", "color": "inherit",
                                         'padding-left': '55rem'},
                                )
                            ]
                        ),

                        # Insert Github Logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "github_logo1.png"))
                            ], href="https://github.com/SulmanK/eBay-web-crawler-phone-auctions",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "dash_banner_v3.png"))
                            ], href="https://dash.plotly.com/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "ebay_logo2.png"))
                            ], href="https://ebay.com/",
                        ),

                    ], className="row",
                )
            ], className="banner", style={'backgroundColor': '#c50063'}
        ),

        # Two Tab Webpage
        html.Div(
            [
                dcc.Tabs(
                    id="tabs-with-classes",
                    value='tab-1-example',
                    parent_className='custom-tabs',
                    className='custom-tabs-container',
                    children=[
                        dcc.Tab(
                            label='About',
                            value='tab-1-example',
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style=tab_style,
                            selected_style=tab_selected_style,
                        ),
                        dcc.Tab(
                            label='Application',
                            value='tab-2-example',
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style=tab_style,
                            selected_style=tab_selected_style,
                        ),
                    ]
                ),
            ]
        ),
        html.Div(id='tabs-content-classes'),
    ],
)
# ------------------- Function Callbacks

# Render the multi-tab web application.


@app.callback(
    Output('tabs-content-classes', component_property='children'),
    [Input(component_id='tabs-with-classes', component_property='value'), ]
)
def render_image(tab):
    if tab == 'tab-1-example':
        return tab_1_layout

    elif tab == 'tab-2-example':
        return tab_2_layout
