from sqlalchemy import orm
import sqlalchemy as sqla
from singletask_sql.tables.utils import Enum
from singletask_sql.tables.base import BaseTable


class State(Enum):
    PROGRESS = 0
    CHECK = 1
    DEFERRED = 2
    DONE = 3
    WAITING_AFTER_ASSIGN = 4

    _mapping = {
        0: 'PROGRESS',
        1: 'CHECK',
        2: 'DEFERRED',
        3: 'DONE',
        4: 'WAITING_AFTER_ASSIGN',
    }


class TasksTable(BaseTable):
    __tablename__ = 'tasks'
    description = sqla.Column(sqla.Text, nullable=False)
    domains = sqla.Column(sqla.Text, nullable=False)
    tags = sqla.Column(sqla.Text, nullable=False)


class TasksCommentsTable(BaseTable):
    __tablename__ = 'tasks_comments'
    text = sqla.Column(sqla.Text, nullable=False)


class TasksStateTable(BaseTable):
    __tablename__ = 'tasks_state'
    state = sqla.Column(sqla.Integer, nullable=False)

    @orm.validates('state')
    def validate_state(self):
        try:
            State.to_string(self.state)
        except IndexError:
            raise ValueError('Invalid state')
