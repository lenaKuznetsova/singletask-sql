from .tables import (TasksTable,
                     BaseTable,
                     TasksCommentsTable,
                     TaskStatesTable,
                     BaseEventsTable,
                     PerformersTable,
                     ManagersEvents,
                     HttpEvents,
                     )
from singletask_sql.tables.entities.tasks import TaskStateType
from singletask_sql.tables.entities.performers import PerformerType
from singletask_sql.tables.entities import events
from singletask_sql.tables import constants as names

tracked_tables = [
    TasksTable,
    TaskStatesTable,
    TasksCommentsTable,
    PerformersTable,
    BaseEventsTable,
    ManagersEvents,
    HttpEvents,
]

events_models = {
    names.TABLE_NAME_MANAGER_EVENTS: ManagersEvents,
    names.TABLE_NAME_HTTP_EVENTS: HttpEvents,
}
