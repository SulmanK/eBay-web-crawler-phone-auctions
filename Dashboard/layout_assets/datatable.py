#--------------------- Packages
import pandas as pd
import dash_table
#--------------------- Datatable
def datatable_asset(df):
    """Function to create a datatable which is used to return the tweets and sentiment."""
    datatable = dash_table.DataTable(
        id='typing_formatting_1',
        data=df.to_dict('records'),
        columns=[
            {
                'id': 'product_name',
                'name': 'Auction',
                'type': 'text'
            },

            {
                'id': 'link',
                'name': 'URL',
                'type': 'text',
                'presentation': 'markdown'
            },

            {
                'id': 'user_feedback',
                'name': 'Feedback',
                'type': 'text'
            },

            {
                'id': 'user_feedback_positive',
                'name': 'Positive feedback (%)',
                'type': 'text'
            },


            {
                'id': 'price',
                'name': 'Price ($)',
                'type': 'numeric'
            },




        ],

        # Highlight Cells based on conditions - first, second, and third row

        style_data_conditional=[


            # Fix columnd widths
            {'if': {'column_id': 'product_name'},
             'width': '20%'},

            {'if': {'column_id': 'link'},
             'width': '20%'},

            {'if': {'column_id': 'user_feedback'},
             'width': '20%'},

            {'if': {'column_id': 'user_feedback_positive'},
             'width': '20%'},


            {'if': {'column_id': 'price'},
             'width': '20%'},


        ],



        # Formatting the data/headers cells
        style_cell={'backgroundColor': '#f7f7f7', 'font-family': 'helvetica',
                    'fontColor': '#000000', 'fontSize': 24, 
                    'textAlign': 'center'
                    },

        style_data={'border': '1px solid LightPink', 'font-size': 24,
                    'font-family': 'helvetica', 'whiteSpace': 'normal',
                    },

        style_header={'border': '1px solid LightPink', 'font-size': 28,
                      'font-family': 'helvetica', 'textAlign': 'center',
                      'fontWeight': 'bold'
                      },

        css=[{
            'selector': '.dash-spreadsheet td div',
            'rule': '''
            line-height: 35px;
            max-height: 35px; min-height: 35px; height: 35px;
            display: block;
            overflow-y: hidden;
            ''',


        }, {'selector': 'table', 'rule': 'table-layout: fixed'}


        ],

        tooltip_data=[{
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        }
            for row in df.to_dict('rows')
        ],

        tooltip_duration=None,
        editable=True,
        page_size=10,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",

    )
    return datatable
