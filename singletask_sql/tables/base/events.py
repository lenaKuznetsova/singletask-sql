import sqlalchemy as sqla
from sqlalchemy.dialects import postgresql

from singletask_sql.tables.base import BaseTable


class EventsTable(BaseTable):
    __tablename__ = 'events'

    data = sqla.Column(postgresql.JSONB, nullable=False)
    domain = sqla.Column(sqla.Text, nullable=True)
    tags = sqla.Column(sqla.Text, nullable=True)
    source = sqla.Column(sqla.Text, nullable=True)
