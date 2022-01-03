import datetime
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class BaseTable(object):
    __mapper_args__ = {
        'confirm_deleted_rows': False
    }

    id = sqla.Column(sqla.Integer, primary_key=True)
    created_at = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())

    # https://www.postgresql.org/docs/9.2/plpgsql-trigger.html
    # auto update postgres triggers "migrations/versions/eedaf2756a19_triggers.py"
    updated_at = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())
    deleted_at = sqla.Column(sqla.DateTime, nullable=True)
