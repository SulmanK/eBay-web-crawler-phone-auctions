# ---------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
# --------------------- Function
def eBayscrapper_clear_tables(phone_model_1, phone_model_2, phone_model_3, phone_model_4):
    """Function to clear psql tables"""
    # PostgreSQL
    # Connect to our database
    DATABASE_URL = "enter"
    engine = create_engine(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    # Perform string manipulations to phone model name
    s_1 = phone_model_1
    s_1 = s_1.lower()
    s_1 = s_1.replace(' ', '_')

    # Perform string manipulations to phone model name
    s_2 = phone_model_2
    s_2 = s_2.lower()
    s_2 = s_2.replace(' ', '_')

    # Perform string manipulations to phone model name
    s_3 = phone_model_3
    s_3 = s_3.lower()
    s_3 = s_3.replace(' ', '_')

    # Perform string manipulations to phone model name
    s_4 = phone_model_4
    s_4 = s_4.lower()
    s_4 = s_4.replace(' ', '_')

    # Drop tables if number of row exceeds 10000
    cursor.execute('DO $do$ BEGIN IF (with cterc as (SELECT COUNT(*) as rn FROM ' + str(s_1) + ' UNION ALL SELECT COUNT(*) FROM ' + str(s_2) + ' UNION ALL SELECT COUNT(*) FROM ' + str(s_3) +
                   ' UNION ALL SELECT COUNT(*) FROM ' + str(s_4) + ') SELECT SUM(rn) as totalrowNo from cterc' + ') > 10000 THEN DROP TABLE ' + str(s_1) + ',' + str(s_2) + ',' + str(s_3) + ',' + str(s_4) + '; END IF; END $do$')

    return "The tables have been cleared."


# ---------------------- Instantiate Function
eBayscrapper_clear_tables(phone_model_1='iPhone 11',
                          phone_model_2='Apple iPhone SE',
                          phone_model_3='Samsung Galaxy Note 10',
                          phone_model_4='Samsung Galaxy S20 Ultra')
