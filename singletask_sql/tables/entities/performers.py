from sqlalchemy import orm
import sqlalchemy as sqla
from singletask_sql.tables.enum import Enum


class PerformerType(Enum):
    TEAM = 0
    DEVELOPER = 1
    MANAGER = 2

    _mapping = {
        0: 'TEAM',
        1: 'DEVELOPER',
        2: 'MANAGER'
    }


class Performers:
    name = sqla.Column(sqla.Text)
    type = sqla.Column(sqla.Integer, index=True)

    domains_whitelist = sqla.Column(sqla.Text, nullable=True)
    tags_whitelist = sqla.Column(sqla.Text, nullable=True)

    domains_blacklist = sqla.Column(sqla.Text, nullable=True)
    tags_blacklist = sqla.Column(sqla.Text, nullable=True)

    @orm.validates('type')
    def validate_assign(self):
        try:
            PerformerType.to_string(self.type)
        except IndexError:
            raise ValueError('Invalid assign type')
