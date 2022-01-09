import sqlalchemy as sqla
from sqlalchemy.dialects import postgresql
from sqlalchemy import orm

from singletask_sql.tables.enum import Enum


class EventType(Enum):
    NEW = 0
    PROCESSED = 1
    RESOLVED = 2

    _mapping = {
        "NEW": 0,
        "PROCESSED": 1,
        "RESOLVED": 2,
    }


class Events:
    data = sqla.Column(postgresql.JSONB)
    type = sqla.Column(sqla.Text, index=True)
    domain = sqla.Column(sqla.Text, nullable=True, index=True)
    tags = sqla.Column(sqla.Text, nullable=True, index=True)
    source = sqla.Column(sqla.Text, nullable=True, index=True)
    table = sqla.Column(sqla.Text, nullable=True, index=True)

    @orm.validates('type')
    def validate_assign(self):
        try:
            EventType.to_string(self.type)
        except IndexError:
            raise ValueError('Invalid assign type')


class HttpEvents:
    code = sqla.Column(sqla.Integer, index=True)
    error = sqla.Column(sqla.Text, index=True)
    link = sqla.Column(sqla.Text)
    response = sqla.Column(sqla.Text)


class ManagerEvents:
    error = sqla.Column(sqla.Text)
    author = sqla.Column(sqla.Text, index=True)
    description = sqla.Column(sqla.Text)
    deadline = sqla.Column(sqla.Text, nullable=True)
    priority = sqla.Column(sqla.Integer)
    performer = sqla.Column(sqla.Text, nullable=True)
