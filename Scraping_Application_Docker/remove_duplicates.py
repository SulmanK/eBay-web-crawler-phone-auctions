# ---------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
# --------------------- Function
def eBayscrapper_remove_duplicates(phone_model):
    """Function to drop duplicate and null rows."""
    # PostgreSQL
    # Connect to our database
    DATABASE_URL = "enter"
    engine = create_engine(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    # Perform string manipulations to phone model name
    s = phone_model
    s = s.lower()
    s = s.replace(' ', '_')

    # Delete columns with null price, timestamp, user, and id values
    cursor.execute('DELETE FROM ' + str(s) +
                   ' WHERE price IS NULL OR user IS NULL or id IS NULL OR timestamp IS NULL;')

    # Delete duplicate values
    cursor.execute('DELETE FROM ' + str(s) +
                   ' WHERE id IN (SELECT id FROM(SELECT  id, ROW_NUMBER() OVER(PARTITION BY id ORDER BY id) AS row_num FROM ' + str(s) + ') t WHERE t.row_num > 1);')
    conn.commit()

    return 'The table has been cleared for duplicate and null values.'


# ---------------------- Instantiate Function
eBayscrapper_remove_duplicates(phone_model='iPhone 11')
eBayscrapper_remove_duplicates(phone_model='Apple iPhone SE')
eBayscrapper_remove_duplicates(phone_model='Samsung Galaxy Note 10')
eBayscrapper_remove_duplicates(phone_model='Samsung Galaxy S20 Ultra')
