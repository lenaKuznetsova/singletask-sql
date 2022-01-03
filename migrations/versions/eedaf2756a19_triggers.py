"""triggers

Revision ID: eedaf2756a19
Revises: 4540f97a6e8e
Create Date: 2022-01-03 21:38:59.894258

"""
from alembic import op
import sqlalchemy as sa
from singletask_sql.tables import tracked_tables

# revision identifiers, used by Alembic.
revision = 'eedaf2756a19'
down_revision = '4540f97a6e8e'
branch_labels = None
depends_on = None

SQL_PROCEDURE = """
CREATE FUNCTION procedure_update() RETURNS trigger AS $procedure_update$
    BEGIN
        NEW.updated_at := timezone('utc', now());
        RETURN NEW;
    END;
$procedure_update$ LANGUAGE plpgsql;

CREATE FUNCTION procedure_delete() RETURNS trigger AS $procedure_update$
    BEGIN
        EXECUTE format('UPDATE %I set deleted_at = now() WHERE id = $1.id', TG_TABLE_NAME)
        USING OLD;
        RETURN NULL;
    END;
$procedure_update$ LANGUAGE plpgsql;
"""

SQl_ADD_TRIGGER_TEMPLATE = """
CREATE TRIGGER trigger_{table_name}_update
    BEFORE UPDATE ON {table_name}
    FOR EACH ROW
    EXECUTE PROCEDURE procedure_update();
    
CREATE TRIGGER trigger_{table_name}_delete
    BEFORE DELETE ON {table_name}
    FOR EACH ROW
    EXECUTE PROCEDURE procedure_delete();
"""

SQL_DELETE_TRIGGER_TEMPLATE = """
DROP TRIGGER trigger_{table_name}_update on {table_name};
DROP TRIGGER trigger_{table_name}_delete on {table_name};
"""


def upgrade():
    # op.execute(SQL_PROCEDURE)
    for table in tracked_tables:
        op.execute(SQl_ADD_TRIGGER_TEMPLATE.format(table_name=table.__tablename__))


def downgrade():
    for table in tracked_tables:
        op.execute(SQL_DELETE_TRIGGER_TEMPLATE.format(table_name=table.__tablename__))
