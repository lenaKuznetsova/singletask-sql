import sqlalchemy as sqla
from sqlalchemy import event
from pprint import pformat

DEBUG_QUERY_TEMPLATE = """{clauseelement}
{params}
"""


def _handle_after_execute(conn, clauseelement, multiparams, params, execution_options, result):
    print(DEBUG_QUERY_TEMPLATE.format(clauseelement=clauseelement, params=pformat(multiparams or params)))


def create_engine(conf, execution_options=None):
    if not execution_options:
        execution_options = {}

    url = sqla.engine.URL.create(
        drivername='postgresql+psycopg2',
        username=conf['POSTGRES_USER'],
        password=conf['POSTGRES_PASSWORD'],
        host=conf['POSTGRES_HOST'],
        port=conf['POSTGRES_PORT'],
        database=conf['POSTGRES_DB']
    )
    engine = sqla.create_engine(url=url)
    if conf["DEBUG_QUERY"] in "1,True,true,yes,on":
        event.listen(engine, "after_execute", _handle_after_execute)

    engine = engine.execution_options(**execution_options)
    return engine
