from pprint import pprint
from sqlalchemy import orm, inspect
from singletask_sql.settings import conf
from singletask_sql.engine import create_engine
from singletask_sql.tables import tracked_tables

conf["DEBUG_QUERY"] = 'off'

engine = create_engine(conf)
# 'default_schema_name', 'dialect', 'engine', 'from_engine', 'get_check_constraints', 'get_columns', 'get_enums',
# 'get_foreign_keys', 'get_foreign_table_names', 'get_indexes', 'get_pk_constraint', 'get_schema_names',
# 'get_sequence_names', 'get_sorted_table_and_fkc_names', 'get_table_comment', 'get_table_names', 'get_table_oid',
# 'get_table_options', 'get_temp_table_names', 'get_temp_view_names', 'get_unique_constraints', 'get_view_definition',
# 'get_view_names', 'has_sequence', 'has_table', 'info_cache', 'reflect_table', 'reflecttable'
inspector = inspect(engine)

sys_state = {
    "exist_tables": inspector.get_table_names(),
    "exist_views": inspector.get_view_names(),
    "indexes": [inspector.get_indexes(table.__tablename__) for table in tracked_tables],
    "tracked_tables": [table.__tablename__ for table in tracked_tables],
    "conf": conf,
    "triggers": None
}

with orm.Session(engine) as session:
    triggers = session.execute("""
        SELECT  event_object_table AS table_name ,trigger_name         
        FROM information_schema.triggers  
        GROUP BY table_name, trigger_name 
        ORDER BY table_name, trigger_name 
        """)
    sys_state["triggers"] = [t for t in triggers]

pprint(sys_state)
