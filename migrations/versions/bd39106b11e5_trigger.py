"""trigger

Revision ID: bd39106b11e5
Revises: 0c746edc7175
Create Date: 2022-01-06 19:35:38.591605

"""
from alembic import op
import sqlalchemy as sa
from singletask_sql.tables import tracked_tables
from singletask_sql.tables.updated_at_triggers import (
    SQL_PROCEDURE,
    SQl_ADD_TRIGGER_TEMPLATE,
    SQL_DELETE_ALL,
)

# revision identifiers, used by Alembic.
revision = 'bd39106b11e5'
down_revision = '0c746edc7175'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(SQL_PROCEDURE)
    for table in tracked_tables:
        op.execute(SQl_ADD_TRIGGER_TEMPLATE.format(table_name=table.__tablename__))


def downgrade():
    for table in tracked_tables:
        op.execute(SQL_DELETE_ALL)

