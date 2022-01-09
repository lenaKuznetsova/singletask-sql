from sqlalchemy import orm
import sqlalchemy as sqla
from singletask_sql.tables.enum import Enum


class TaskStateType(Enum):
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


class Tasks(object):
    description = sqla.Column(sqla.Text)
    domains = sqla.Column(sqla.Text, index=True)
    tags = sqla.Column(sqla.Text, index=True)
    events_table = sqla.Column(sqla.Text, index=True)


class TaskComments(object):
    text = sqla.Column(sqla.Text)


class TaskStates(object):
    state = sqla.Column(sqla.Integer)

    @orm.validates('state')
    def validate_state(self):
        try:
            TaskStateType.to_string(self.state)
        except IndexError:
            raise ValueError('Invalid state')
