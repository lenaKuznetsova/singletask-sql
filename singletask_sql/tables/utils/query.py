from singletask_sql.tables.constants import INCLUDED_DELETED


def include_deleted(query):
    return query.execution_options(**{INCLUDED_DELETED: True})
