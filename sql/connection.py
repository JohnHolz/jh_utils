from sqlalchemy import create_engine
import psycopg2

def create_connection(database, user, password, host, port, sgbd = 'postgresql'):
    ## Creating connections
    if sgbd == 'postgresql':
        con_string = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
    if sgbd == 'mysql':
        con_string = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
    return create_engine(con_string)