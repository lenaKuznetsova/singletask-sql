import datetime
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseTable(object):
    @declared_attr
    def id(self):
        return sqla.Column(sqla.Integer, primary_key=True)

    @declared_attr
    def created_at(self):
        return sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())

    updated_at = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())
    deleted_at = sqla.Column(sqla.DateTime, nullable=True)
