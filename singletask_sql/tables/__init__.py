from .tables import (TasksTable,
                     BaseTable,
                     TasksCommentsTable,
                     TaskStatesTable,
                     EventsTable,
                     PerformersTable,
                     )
from singletask_sql.tables.entities.tasks import TaskStateType
from singletask_sql.tables.entities.performers import PerformerType

tracked_tables = [
    TasksTable,
    TaskStatesTable,
    TasksCommentsTable,
    PerformersTable,
    EventsTable
]
