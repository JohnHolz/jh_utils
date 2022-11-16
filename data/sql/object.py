from jh_utils.data.sql.connection import create_connection, create_string_connection
from jh_utils.data.sql.manipulate_db import create_table_structure, get_tables, drop_table, delete_table, get_top_rows, get_schemas, create_schema, drop_schema, apply_delete_to_schema
from dotenv import dotenv_values
from sqlalchemy import inspect

doc = """
    env: db, user, pass, host, port
    ----------------------------
    example .env
    host=weather
    host1=weather
    db=weather
    user=weather
    pass=weather12
    port=5400
    schema=raw
    """


class DB():
    doc
    def __init__(self,db,user,password,host,port):
        self.db = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.uri = create_string_connection(database=self.db,
                            user=self.user,
                            password=self.password,
                            host=self.host,
                            port=self.port)
        self.engine = '--empty--'
        
    def connect(self):
        __doc__ = """
        Fill self.engine with sqlalchemy connection
        """
        self.engine = create_connection(database=self.db,
                            user=self.user,
                            password=self.password,
                            host=self.host,
                            port=self.port)

    def __repr__(self) -> str:
        return f"""host: {self.host}\ndb:{self.db}"""


    ## ! table
    def drop_table(self, table,schema):
        return drop_table(table,schema=schema,engine=self.engine)
    
    def delete_table(self,table_name,schema):
        delete_table(table_name, schema, self.engine, close_connection = True)

    def get_schemas(self):
        return get_schemas(self.engine)
    
    def get_tables(self,schema):
        return get_tables(schema,self.engine)
    
    def get_top_rows(self, table, schema, n=5):
        return get_top_rows(table = table, schema = schema, engine = self.engine, n=n)

    ## ! schema
    def drop_schema(self, schema):
        drop_schema(schema=schema,engine = self.engine)
    
    def create_schema(self, schema_nema):
        create_schema(schema_nema, self.engine)
        
    def run_sql(self, sql):
        conn = self.engine.connect()
        conn.execute(sql)

##
## ? Second form to create the object
## 

def create_object_DB(env_dict):
    doc
    db = DB(db = env_dict['db'],user = env_dict['user'],password = env_dict['pass'],host = env_dict['host'],port = env_dict['port'])
    return db
        
def create_object_DB_by_envfile(path='.env'):
    doc
    env = dotenv_values(path)
    db = create_object_DB(env)
    return db

