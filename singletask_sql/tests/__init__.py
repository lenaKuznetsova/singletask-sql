from unittest import TestCase

from singletask_sql.settings import conf
from singletask_sql.engine import create_engine


class DBTestCase(TestCase):
    sql_engine = create_engine(conf)
