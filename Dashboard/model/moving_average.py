#--------------------- Packages
import datetime
import numpy as np
import pandas as pd
# --------------------- Moving Average
def moving_average_df(df):
    "Function to create dataframes to calculate the moving average."
    # Preprocess initial dataframes
    df['timestamp_m-d'] = df['timestamp'].apply(
        lambda x: datetime.datetime.strftime(x, '%B-%d'))
    df['dayofyear'] = df['timestamp'].apply(
        lambda x: datetime.datetime.strftime(x, '%j'))

    # Create new dataframe to calculate average price per day
    tmp = df[['price', 'dayofyear']].groupby('dayofyear').mean()
    tmp_df = pd.DataFrame(data={'mean_price': tmp['price'].values,
                                'dayofyear': tmp['price'].index})

    # Create a datetime date column
    tmp_df['date'] = tmp_df['dayofyear'].apply(
        lambda x: datetime.datetime.strptime(str(x), '%j').strftime('%b-%d'))
    tmp_df['date'] = tmp_df['date'].apply(
        lambda x: datetime.datetime.strptime(x, '%b-%d'))
    return tmp_df
