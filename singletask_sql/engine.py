import sqlalchemy as sqla
from sqlalchemy import event

def create_engine(conf):
    url = sqla.engine.URL.create(
        drivername='postgresql+psycopg2',
        username=conf['POSTGRES_USER'],
        password=conf['POSTGRES_PASSWORD'],
        host=conf['POSTGRES_HOST'],
        port=conf['POSTGRES_PORT'],
        database=conf['POSTGRES_DB']
    )

    return sqla.create_engine(url=url)
