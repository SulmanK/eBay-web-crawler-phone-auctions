#--------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import bs4
import numpy as np
import pandas as pd
import psycopg2
import requests
# --------------------- Active Auctions
# Check if a variable is in the list
def check_active(x, list_1):
    """check if a variable is in the list"""
    if x in list_1:
        x = 'NO'
    else:
        x = 'YES'
    return x

# Labels auctions that are active or inactive
def active_auctions_ids(phone_model):
    "Function to retrieve active auctions"
    inactive_url = []
    
    try:
        
        # Pull the data from the database
        # Set up the connection
        DATABASE_URL = "postgres://isczffxjpjzpxr:41e6aaa55dd93e8ae680b5d6ab8eef4febc02f2a94b7c266dffce8ccea74c286@ec2-50-19-26-235.compute-1.amazonaws.com:5432/d64tko6dss9lgk"
        engine = create_engine(DATABASE_URL)
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        # Perform string manipulations to phone model name
        s = phone_model
        s = s.lower()
        s = s.replace(' ', '_')

        # Store the data into their respective dataframes
        df = pd.read_sql('select * from ' + str(s) , con=conn, index_col = 'index')
        df.index = [x for x in range (0, len(df))]

        # Iterate through all the urls in the dataframe
        for x in df[df['active_auction'] == 'YES']['url'][0:100]:
            
            # First case: Check if listing has ended using the top panel
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

            # Check if listing has ended using the yellow text
            try:
                # Initiate requests
                r = requests.get(x)

                # Get text data
                text_data = r.text
                soup = bs4.BeautifulSoup(text_data, "html.parser")

                # Other cases
                tmp = soup.find(
                    'span', attrs={'class': 'msgTextAlign'})

                if tmp.find(text = True) != None:
                    inactive_url.append(x)
                    
            except:
                None

        # Change all entries if they are active or inactive
        df['active_auction'] = df['url'].apply(
            lambda x: check_active(x=x, list_1=inactive_url))

        # Drop original table from database
        cursor.execute('DROP TABLE IF EXISTS' + ' ' + str(s))
        conn.commit()

        # Insert df to database
        df.to_sql(str(s), con=engine, if_exists='fail')
        conn.commit()
        conn.close()
   
    except:
        conn.close()
        print('Query failed to execute')
    
    return print("The data entries have been added for " + str(s))
    
# Instantiate Functions
active_auctions_ids(phone_model = 'iPhone 11')
active_auctions_ids(phone_model = 'Apple iPhone SE')
active_auctions_ids(phone_model = 'Samsung Galaxy Note 10')
active_auctions_ids(phone_model = 'Samsung Galaxy S20 Ultra')