from jh_utils.pandas.sql import get_data

def get_first_row(table, schema, engine):
    return get_data(f'select * from {schema}.{table} dc limit 1',engine)

def create_table_structure(pandas_df, table_name, engine, schema, index = False, if_exists = 'append'):
    pandas_df.to_sql(name = table_name,
                    con = engine, 
                    schema=schema, index=index, if_exists = if_exists)
    conn = engine.connect()
    conn.execute(f'DELETE FROM {schema}.{table_name}')
    conn.close()