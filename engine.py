from singletask_sql.settings import conf
import sqlalchemy as sqla
from sqlalchemy.ext import declarative as sqla_declarative

URL = sqla.engine.URL.create(
    drivername='postgresql+psycopg2',
    username=conf['POSTGRES_USER'],
    password=conf['POSTGRES_PASSWORD'],
    host=conf['POSTGRES_HOST'],
    port=conf['POSTGRES_PORT'],
    database=conf['POSTGRES_DB']
)
engine = sqla.create_engine(url=URL)

