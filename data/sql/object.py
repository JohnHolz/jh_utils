from connection import create_connection, create_string_connection
from dotenv import dotenv_values
from manipulate_db import get_schemas, get_tables, get_top_rows

class db():
    
    """
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
    
    def __init__(self,path='.env'):
        self.path = path
        self.env = dotenv_values(path)

    def connect(self):
        self.uri = create_string_connection(database=self.env['db'],
                            user=self.env['user'],
                            password=self.env['pass'],
                            host=self.env['host'],
                            port=self.env['port'])
        self.engine = create_connection(database=self.env['db'],
                            user=self.env['user'],
                            password=self.env['pass'],
                            host=self.env['host'],
                            port=self.env['port'])

    def get_schemas(self):
        return get_schemas(self.engine)
    
    def get_tables(self,schema):
        return get_tables(schema,self.engine)
    
    def get_top_rows(self, table, schema, n=5):
        get_top_rows(table = table, schema = schema, engine = self.engine, n=n)