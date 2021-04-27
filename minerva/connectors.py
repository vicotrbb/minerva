import sqlalchemy
from sqlalchemy import create_engine


def get_default_connector():
    engine = create_engine("sqlite:///default.db", echo=True, future=True)
    return engine.connect()


def get_custom_connector(conn):
    if type(conn) != 'str':
        conn = f''  # TO-DO

    engine = create_engine(conn, echo=True, future=True)
    return engine.connect()
