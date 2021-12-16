# ---------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

# --------------------- Function


def eBayscrapper_remove_duplicates(phone_model):
    """Function to drop duplicate and null rows."""
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

        # Delete columns with null price, timestamp, user, and id values
        cursor.execute('DELETE FROM ' + str(s) +
                       ' WHERE (user IS NULL) OR (price IS NULL) OR (user_feedback IS NULL) OR (user_feedback_positive IS NULL) OR (id is NULL) OR (timestamp is NULL);')

        # Commit changes
        conn.commit()

        # Delete duplicate values
        cursor.execute('DELETE FROM ' + str(s) +
                       ' x USING ' + str(s) + ' y WHERE x.index > y.index AND x.id = y.id;')

        # Commit changes
        conn.commit()

        # Close cursor
        cursor.close()

        # Close connection
        conn.close()

    except:
        # Close Cursor
        cursor.close()

        # Close Connection
        conn.close()
        print('Error in previous query')

    return "The tables have been cleared"


# ---------------------- Instantiate Function
eBayscrapper_remove_duplicates(phone_model='iPhone 11')
eBayscrapper_remove_duplicates(phone_model='Apple iPhone SE')
eBayscrapper_remove_duplicates(phone_model='Samsung Galaxy Note 10')
eBayscrapper_remove_duplicates(phone_model='Samsung Galaxy S20 Ultra')
