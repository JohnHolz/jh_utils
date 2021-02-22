## importing libs
import pandas as pd
from sqlalchemy import create_engine
import json
import psycopg2

def create_connection(database, user, password, host, port, sgbd = 'postgresql'):
    ## Creating connections
    if sgbd == 'postgresql':
        con_string = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
    if sgbd == 'mysql':
        con_string = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
    return create_engine(con_string)

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