from singletask_sql.tests import DBTestCase
from sqlalchemy import orm
from sqlalchemy import func
from singletask_sql.tables import TasksTable
from singletask_sql.tables.utils import query as query_utils


# https://docs.sqlalchemy.org/en/14/orm/query.html


def create_task(description):
    task = TasksTable()
    task.description = description
    task.domains = f"{description} domains"
    task.tags = f"{description} tasks"
    return task


class TaskTestCase(DBTestCase):

    def test(self):
        with orm.Session(self.sql_engine) as session:
            query = session.query(func.count(TasksTable.id))
            result = session.execute(query).all()
            print(result)

            query = session.query(func.count(TasksTable.id))
            query = query_utils.include_deleted(query)
            result = session.execute(query).all()
            print(result)
