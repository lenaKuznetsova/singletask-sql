from singletask_sql.tests import DBTestCase
from sqlalchemy import orm

from singletask_sql.tables import TasksTable, TasksCommentsTable


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
            task = create_task("test")
            task_del = create_task("test del")
            session.add(task, task_del)
            session.delete(task_del)
            session.commit()

    # def test_1(self):
    #     with orm.Session(self.sql_engine) as session:
    #         task = TasksTable()
    #         task.description = "test"
    #         task.domains = ""
    #         task.tags = ""
    #         session.add(task)
    #
    #         comment = TasksCommentsTable()
    #         comment.text = "some_text"
    #         comment.task = task
    #
    #         session.add(comment)
    #         session.commit()
    #
    #         print(task.id)
    #         print(comment.task_id)
