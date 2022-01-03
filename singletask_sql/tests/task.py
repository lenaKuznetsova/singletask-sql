from singletask_sql.tests import DBTestCase
from unittest import TestCase
from dotenv import dotenv_values
from sqlalchemy import orm

from singletask_sql.settings import BASE_DIR
from singletask_sql.engine import create_engine
from singletask_sql.tables.base.performers import PerformersTable


class TaskTestCase(DBTestCase):

    def test_1(self):
        with orm.Session(self.sql_engine) as session:
            model = PerformersTable()
            model.name = "lena"
            session.add(model)
            session.commit()

            model_id = model.id

            print(model_id)

            session.delete(model)
            session.commit()

            print(model.id)
