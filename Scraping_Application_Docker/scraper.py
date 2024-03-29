# --------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import bs4
import datetime as dt
import pandas as pd
import psycopg2
import re
import requests
import time
# --------------------- Function


def eBayscrapper_daily(phone_model):
    """Function to scrape the phone prices off eBay"""
    # Create item and price list
    item_name = []
    prices = []
    item_urls = []
    item_timestamps = []
    item_ids = []
    user_name = []
    user_feedback = []
    user_pos = []

    # Logic for selecting url for phone models
    if phone_model == 'iPhone 11':

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=iPhone+11&_sacat=0&LH_TitleDesc=0&_sop=10&_ipg=25&_pgn=1'

    elif phone_model == 'Apple iPhone SE':

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=Apple+iPhone+SE&_sacat=0&LH_TitleDesc=0&_sop=10&_ipg=25&_pgn=1'

    elif phone_model == 'Samsung Galaxy Note 10':

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=Samsung+Galaxy+Note+10&_sacat=0&LH_TitleDesc=0&_sop=10&_ipg=25&_pgn=1'

    elif phone_model == 'Samsung Galaxy S20 Ultra':

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=Samsung+Galaxy+S20+Ultra&_sacat=0&LH_TitleDesc=0&_sop=10&_ipg=25&_pgn=1'

    else:
        print("Don't have that phone listed.")

    # First phase to collect product names, prices, urls, and timestamps
    # Initiate requests module
    r = requests.get(url)

    # Examine the text data from the requests page
    text_data = r.text

    # Utilize beautiful soup to examine the html tags for specific contents
    soup = bs4.BeautifulSoup(text_data, "html.parser")

    # Examine the body content of the html tags for auction specifics
    listings = soup.find_all('li', attrs={'class': 's-item'})

    # Create a loop to iterate through each auction listing.
    for listing in listings:
        prod_name = " "
        prod_price = " "
        prod_url = " "
        prod_timestamp = " "

        # Iterate through each name in listing to obtain the product name and price
        for name, href_urls in zip(listing.find_all('h3', attrs={'class': "s-item__title"}),
                                   listing.find_all(
                                       'a', attrs={'class': "s-item__link"}),
                                   ):

            # Append the product name
            #print(str(name.find(text = True, recursive = False)))
            if(str(name.find(text=True, recursive=False)) != "None"):
                prod_name = str(name.find(text=True, recursive=False))
                item_name.append(prod_name)

            # Append product price
            if(prod_name != " "):

                # Extract prices
                price = listing.find('span', attrs={'class': "s-item__price"})
                prod_price = str(price.find(text=True, recursive=False))

                # Extract href
                href = href_urls['href']
                item_urls.append(href)

                # Extract timestamp
                tmp_timestamp = listing.find(
                    'span',
                    attrs={'class': 's-item__dynamic s-item__listingDate'})

                if tmp_timestamp == None:
                    prod_timestamp = None
                    item_timestamps.append(prod_timestamp)
                else:
                    timestamp = tmp_timestamp.find(
                        'span', attrs={'class': "BOLD"})
                    prod_timestamp = str(timestamp.find(
                        text=True, recursive=False))
                    item_timestamps.append(prod_timestamp)

                # Check if product price is unknown or known
                if prod_price == 'None':
                    prod_price = None
                    prices.append(prod_price)
                else:
                    prod_price = int(
                        re.sub(",", "",
                               prod_price.split("$")[1].split(".")[0]))
                    prices.append(prod_price)

    # Second phase to extract product ids, user, feedback score, and postiive feedback %
    for url in item_urls:
        prod_ids = " "
        prod_user = " "
        prod_feedback = " "
        prod_pos = " "

        # Initiate requests module
        r = requests.get(url)

        # Examine the text data from the requests page
        text_data = r.text

        # Utilize beautiful soup to examine the html tags for specific contents
        soup = bs4.BeautifulSoup(text_data, "html.parser")

        # Extract the item ids
        ebay_ids = soup.find(
            'div', attrs={'class': 'u-flL iti-act-num itm-num-txt'})

        if ebay_ids == None:

            prod_ids = None

            item_ids.append(prod_ids)

        else:
            prod_ids = str(ebay_ids.find(text=True, recursive=False))

            item_ids.append(prod_ids)

        # Extract user names
        user = soup.find(
            'span', attrs={'class': 'ux-textspans--PSEUDOLINK ux-textspans--BOLD'})

        if user == None:

            prod_user = None

            user_name.append(prod_user)

        else:
            prod_user = user.get_text()

            user_name.append(prod_user)

        # Extract feedback score
        feedback = soup.find(
            'div', attrs={'class': 'ux-seller-section__item--seller'})

        # Try and Except block (we use this because we are indexing on the tags, if there isnt an index that means its a null)
        try:

            feedback = feedback.find_all(
                'span', attrs={'class': 'ux-textspans--PSEUDOLINK'})[1]

            if feedback == None:

                prod_feedback = None

                user_feedback.append(prod_feedback)

            else:
                prod_feedback = feedback.get_text()

                user_feedback.append(prod_feedback)
        except:
            prod_feedback = None

            user_feedback.append(prod_feedback)

        # Extract positive feedback %
        # Examine div tag

        # Try and Except block (we use this because we are indexing on the tags, if there isnt an index that means its a null)
        try:
            pos_feedback = soup.find_all(
                'div', attrs={'class': 'ux-seller-section__item'})[1]

            # Examine span tag
            pos_feedback = pos_feedback.find('span')

            if pos_feedback == None:

                prod_pos = None

                user_pos.append(prod_pos)
            else:
                prod_pos = pos_feedback.get_text()

                prod_pos = re.findall("\d+", prod_pos)[0]

                user_pos.append(prod_pos)
        except:
            prod_pos = None

            user_pos.append(prod_pos)

    # Dataframe
    df = pd.DataFrame(data={'product_name': item_name,
                            'url': item_urls,
                            'id': item_ids,
                            'creation': item_timestamps,
                            'user': user_name,
                            'user_feedback': user_feedback,
                            'user_feedback_positive': user_pos,
                            'price': prices})

    # Datetime conversion
    # String manipulation
    df['timestamp'] = df['creation'].apply(lambda x: x.replace('-', ' '))
    df['timestamp'] = df['timestamp'].apply(lambda x: x.replace(' ', ':'))

    # Replace month text
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Jan', 'January'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Feb', 'February'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Mar', 'March'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Apr', 'April'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('May', 'May'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Jun', 'June'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Jul', 'July'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Aug', 'August'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Sep', 'September'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Oct', 'October'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Nov', 'November'))
    df['timestamp'] = df['timestamp'].apply(
        lambda x: x.replace('Dec', 'December'))

    # Convert timestmap to datetime
    df['timestamp'] = df['timestamp'].apply(lambda x:
                                            dt.datetime.strptime(x, '%B:%d:%H:%M'))

    # Creat new column listing month of each auction
    df['month'] = pd.DatetimeIndex(df['timestamp']).month

    # Drop entries that are greater than creation
    df = df[df['month'] <= dt.datetime.now().month]

    # Add active auctions column
    df['active_auction'] = 'YES'

    # Drop entries with null user, user_feedback, user_feedback_pos, and price
    df = df.drop(
        df.loc[
            (df['user'] == None) | (df['user_feedback'] == None) | (
                df['user_feedback_positive'] == None) | (df['price'] == None)
        ].index).reset_index(drop=True)
    try:
        # PostgreSQL
        # Connect to our database
        DATABASE_URL = "postgres://isczffxjpjzpxr:41e6aaa55dd93e8ae680b5d6ab8eef4febc02f2a94b7c266dffce8ccea74c286@ec2-50-19-26-235.compute-1.amazonaws.com:5432/d64tko6dss9lgk"
        engine = create_engine(DATABASE_URL)
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()

        # Perform string manipulations to phone model name
        s = phone_model
        s = s.lower()
        s = s.replace(' ', '_')

        # Write dataframe to SQL database
        try:
            df.to_sql(str(s), con=engine, if_exists='append')
            conn.commit()

        except:
            print('error')

        # Read in dataframe from SQL
        tmp_df = pd.read_sql('select * from ' + str(s),
                             con=conn, index_col='index')
        tmp_df.index = [x for x in range(0, len(tmp_df))]

        # Drop original table from database
        cursor.execute('DROP TABLE IF EXISTS' + ' ' + str(s))

        # Commit changes
        conn.commit()

        # Write dataframe to SQL database
        tmp_df.to_sql(str(s), con=engine, if_exists='fail')

        # Commit changes
        conn.commit()

        # Close cursor and connections
        cursor.close()
        conn.close()

    except:
        # Close cursor and connections
        cursor.close()
        conn.close()
        print('Error in previous query.')

    return print("The data entries have been added for " + str(s))


# ---------------------- Instantiate Function
eBayscrapper_daily(phone_model='iPhone 11')
eBayscrapper_daily(phone_model='Apple iPhone SE')
eBayscrapper_daily(phone_model='Samsung Galaxy Note 10')
eBayscrapper_daily(phone_model='Samsung Galaxy S20 Ultra')
