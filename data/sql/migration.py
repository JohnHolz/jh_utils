from jh_utils.pandas import sql
import dask as dd

def pandas_migrate_table(query, table_name, engine_origin, engine_destiny, destiny_schema, if_exists):
    df = sql.get_data(query, engine_origin)
    sql.write_table(df, table_name, destiny_schema, engine_destiny,
                    if_exists=if_exists, chunksize=10_000, index=False, close_connection=False)

def pandas_migrate_function(engine_origin, 
                         engine_destiny, 
                         destiny_schema,index=False):
    def output_func(query, table_name, if_exists='replace', chunksize=10_000):
        df = sql.get_data(query, engine_origin)
        sql.write_table(df, table_name, destiny_schema, engine_destiny,
                        if_exists=if_exists, chunksize=10_000, 
                        index=False, close_connection=False)
    return output_func


def dask_migrate_table(table,
                       table_id,
                       input_schema,
                       output_schema,
                       uri_input,
                       uri_output,
                       npartitions,
                       bytes_per_chunk='256MB',
                       parallel=True,
                       if_exists='append',
                       method='multi'):
    df = dd.read_sql_table(table=table,
                           uri=uri_input,
                           schema=input_schema,
                           index_col=table_id,
                           npartitions=npartitions,
                           bytes_per_chunk=bytes_per_chunk)
    df = df.drop(f'{table_id}__1', axis=1)
    dd.to_sql(df,
              uri=uri_output,
              name=table,
              schema=output_schema,
              if_exists=if_exists,
              parallel=parallel,
              method=method)


def dask_migrate_function(uri_input, uri_output):
    def output_func(table, 
                    table_id, 
                    input_schema, 
                    output_schema, 
                    npartitions, 
                    bytes_per_chunk='256MB', 
                    parallel=True, 
                    if_exists='append', 
                    method='multi'):
        df = dd.read_sql_table(table=table,
                               uri=uri_input,
                               schema=input_schema,
                               index_col=table_id,
                               npartitions=npartitions,
                               bytes_per_chunk=bytes_per_chunk)
        df = df.drop(f'{table_id}__1', axis=1)
        dd.to_sql(df,
                  uri=uri_output,
                  name=table,
                  schema=output_schema,
                  if_exists=if_exists,
                  parallel=parallel,
                  method=method)
    return output_func
