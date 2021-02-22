## importing libs
import pandas as pd
import json
from sqlalchemy import create_engine
import psycopg2

def get_data(query, engine):
    engine.connect()
    table = pd.read_sql(query, engine)
    return table

def write_table(table, table_name, schema, engine, if_exists = 'append', index= False):
    engine.connect()
    ## write or replace table
    table.to_sql(name = table_name,
                 if_exists = if_exists,
                 con = engine,
                 schema=schema,
                 method='multi',
                 index = index)