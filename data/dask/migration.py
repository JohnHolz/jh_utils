import dask as dd

def send_table(table,
               table_id, 
               input_schema, 
               output_schema, 
               uri_input, 
               uri_output, 
               npartitions, 
               bytes_per_chunk='256MB',
               parallel = True,
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