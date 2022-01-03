from singletask_sql.tests import DBTestCase
from sqlalchemy import orm

from singletask_sql.tables.base.performers import PerformersTable


class MySession(orm.Session):
    pass


class TaskTestCase(DBTestCase):

    def test_1(self):
        with orm.Session(self.sql_engine) as session:
            pass
