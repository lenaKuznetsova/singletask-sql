import sqlalchemy as sqla
from sqlalchemy.dialects import postgresql


class Events:
    data = sqla.Column(postgresql.JSONB)
    domain = sqla.Column(sqla.Text, nullable=True)
    tags = sqla.Column(sqla.Text, nullable=True)
    source = sqla.Column(sqla.Text, nullable=True)
