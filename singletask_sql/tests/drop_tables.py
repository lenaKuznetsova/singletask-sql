from singletask_sql.tests import DBTestCase
from sqlalchemy import orm


class TaskTestCase(DBTestCase):
    def test_1(self):
        with orm.Session(self.sql_engine) as session:
            for table in ['alembic_version', 'tasks', 'events', 'performers', 'task_states', 'task_comments',
                          'tasks_comments', 'tasks_state', 'task_comments']:
                try:
                    session.execute(f'drop table public.{table} CASCADE;')
                except Exception as ex:
                    print(ex)
                session.commit()

            try:
                session.execute('DROP FUNCTION procedure_update CASCADE;')
            except Exception as ex:
                print(ex)
            session.commit()
