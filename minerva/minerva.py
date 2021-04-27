import numpy
from .engines import sql_engine, web_server
from . import helpers
from . import connectors


class Minerva:
    def __init__(self, url='http://localhost', port=int('5000'), database='sqlite3', use_web_server=True, conn=None, tables=[], gen_from_database=False, **kwargs):
        if not conn:
            self.conn = connectors.get_default_connector()
        else:
            self.conn = connectors.get_custom_connector(conn)

        self.engine = sql_engine.SqlEngine(self.conn)
        self.database = database
        self.tables = tables
        self.use_web_server = use_web_server
        self.url = url
        self.port = port
        self.server_url = f'{url}:{port}/'

        if gen_from_database:
            self.generate_from_database()

        if use_web_server:
            self.start_server()

        if kwargs:
            self.process_kwargs()

    def set_connection(self, conn):
        self.conn = connectors.get_custom_connector(conn)
        self.engine = sql_engine.SqlEngine(self.conn)

    def start_server(self):
        pass

    def stop_server(self):
        pass

    def add_table(self, table, public=True):
        pass

    def generate_from_database(self):
        pass

    def process_kwargs(self, kwargs):
        if 'web_server_conf' in kwargs:
            self.web_server_conf = kwargs
