# --------------------- Packages
import numpy as np
import pandas as pd
import psycopg2
# --------------------- Data Gathering
""" Script to pull the scraped eBay data from the PostgreSQL database, retrieves the dataframe and initializes various variables for analysis."""
# Pull the data from the database
# Set up the connection
DATABASE_URL = "enter"
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Store the data into their respective dataframes
df_ip11 = pd.read_sql('select * from iphone_11', con=conn)
df_ipse = pd.read_sql('select * from apple_iphone_se', con=conn)
df_sg10 = pd.read_sql('select * from samsung_galaxy_note_10', con=conn)
df_sg20 = pd.read_sql('select * from samsung_galaxy_s20_ultra', con=conn)

# Create a new column (will use for naming the categorical axes)
df_ip11['model'] = 'iPhone 11'
df_ipse['model'] = 'iPhone SE'
df_sg10['model'] = 'Note 10'
df_sg20['model'] = 'S20 Ultra'

# Change user feeback rating into an integer
df_ip11['user_feedback'] = df_ip11['user_feedback'].apply(lambda x: int(x))
df_ipse['user_feedback'] = df_ipse['user_feedback'].apply(lambda x: int(x))
df_sg10['user_feedback'] = df_sg10['user_feedback'].apply(lambda x: int(x))
df_sg20['user_feedback'] = df_sg20['user_feedback'].apply(lambda x: int(x))

# Change user_feedback into a stars rating format
def user_feedback_rating(x):
    """Function to create an emoji's star rating format given intervals"""

    if x <= 100:
        x = '⭐'

    elif (x > 100) & (x <= 499):
        x = '⭐⭐'

    elif (x > 499) & (x <= 999):
        x = '⭐⭐⭐'

    elif (x > 999) & (x <= 4999):
        x = '⭐⭐⭐⭐'

    elif x > 4999:
        x = '⭐⭐⭐⭐⭐'

    else:
        x = 'No rating'

    return x


# Instantiate function
df_ip11['user_feedback'] = df_ip11['user_feedback'].apply(
    lambda x: user_feedback_rating(x))
df_ipse['user_feedback'] = df_ipse['user_feedback'].apply(
    lambda x: user_feedback_rating(x))
df_sg10['user_feedback'] = df_sg10['user_feedback'].apply(
    lambda x: user_feedback_rating(x))
df_sg20['user_feedback'] = df_sg20['user_feedback'].apply(
    lambda x: user_feedback_rating(x))

# Remove % from positive feedback score
def replace_none_values(x):
    "Function to replace null values and remove percent signs"
    if x == None:

        x = 'None'

    else:
        x = x.replace('%', '')

    return x


# Instantiate Function
df_ip11['user_feedback_positive'] = df_ip11['user_feedback_positive'].apply(
    lambda x: replace_none_values(x))
df_ipse['user_feedback_positive'] = df_ipse['user_feedback_positive'].apply(
    lambda x: replace_none_values(x))
df_sg10['user_feedback_positive'] = df_sg10['user_feedback_positive'].apply(
    lambda x: replace_none_values(x))
df_sg20['user_feedback_positive'] = df_sg20['user_feedback_positive'].apply(
    lambda x: replace_none_values(x))

# HTML representation
def f(row):
	"""Function which provides the html representation of a link, will be needed for datatable"""
	l = "[{0}]({0})".format(row["url"])
	return l

# Get the html format for links
df_ip11["link"] = df_ip11.apply(f, axis=1)
df_ipse["link"] = df_ipse.apply(f, axis=1)
df_sg10["link"] = df_sg10.apply(f, axis=1)
df_sg20["link"] = df_sg20.apply(f, axis=1)
