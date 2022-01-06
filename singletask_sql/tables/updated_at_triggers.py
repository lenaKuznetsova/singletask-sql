SQL_PROCEDURE = """
CREATE FUNCTION procedure_update() RETURNS trigger AS $procedure_update$
    BEGIN
        NEW.updated_at := timezone('utc', now());
        RETURN NEW;
    END;
$procedure_update$ LANGUAGE plpgsql;
"""

SQl_ADD_TRIGGER_TEMPLATE = """
CREATE TRIGGER trigger_{table_name}_update
    BEFORE UPDATE ON {table_name}
    FOR EACH ROW
    EXECUTE PROCEDURE procedure_update();
"""

SQL_DELETE_ALL = """
DROP PROCEDURE procedure_update CASCADE;
"""
