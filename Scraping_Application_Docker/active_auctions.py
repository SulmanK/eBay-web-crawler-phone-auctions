#--------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import bs4
import numpy as np
import pandas as pd
import psycopg2
import requests
# --------------------- Active Auctions
# Pull the data from the database
# Set up the connection
DATABASE_URL = "enter"
engine = create_engine(DATABASE_URL)
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Store the data into their respective dataframes
df_ip11 = pd.read_sql('select * from iphone_11', con=conn,)
df_ipse = pd.read_sql('select * from apple_iphone_se', con=conn)
df_sg10 = pd.read_sql('select * from samsung_galaxy_note_10', con=conn)
df_sg20 = pd.read_sql('select * from samsung_galaxy_s20_ultra', con=conn)

# Check if a variable is in the list


def check_active(x, list_1):
    if x in list_1:
        x = 'YES'
    else:
        x = 'NO'
    return x

# Labels auctions that are active or inactive


def active_auctions_ids(df, phone_model):
    "Function to retrieve active auctions"
    inactive_url = []
    # Iterate through all the urls in the dataframe
    for x in df[df['active_auction'] == 'YES']['url']:
        try:
            # Initiate requests
            r = requests.get(x)

            # Get text data
            text_data = r.text
            soup = bs4.BeautifulSoup(text_data, "html.parser")

            # Extract the active auction urls
            tmp = soup.find(
                'div', attrs={'class': 'nodestar-item-card-details__header-text'})
            tmp_active = tmp.find('span')
            tmp_active_auction = str(tmp_active.find(text=True))

            # If this string is present, append the url to the list.
            if tmp_active_auction == "The listing you're looking for has ended.":
                inactive_url.append(x)
        except:
            None

    # Change all entries if they are active or inactive
    df['active_auction'] = df['url'].apply(
        lambda x: check_active(x=x, list_1=inactive_url))

    # PostgreSQL database

    # Perform string manipulations to phone model name
    s = phone_model
    s = s.lower()
    s = s.replace(' ', '_')

    # Drop original table from database
    cursor.execute('DROP TABLE IF EXISTS' + ' ' + str(s))
    conn.commit()

    # Insert df to database
    df.to_sql(str(s), con=engine, if_exists='append')
    conn.commit()

    return print("The data entries have been added for " + str(s))

# Instantiate Functions
active_auctions_ids(df = df_ip11, phone_model = 'iPhone 11')
active_auctions_ids(df = df_ipse, phone_model = 'Apple iPhone SE')
active_auctions_ids(df = df_sg10, phone_model = 'Samsung Galaxy Note 10')
active_auctions_ids(df = df_sg20, phone_model = 'Samsung Galaxy S20 Ultra')