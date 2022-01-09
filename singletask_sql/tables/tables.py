import datetime
import sqlalchemy as sqla
from sqlalchemy import orm
from sqlalchemy import event
from sqlalchemy.ext.declarative import as_declarative

from singletask_sql.tables.entities import tasks
from singletask_sql.tables.entities import performers
from singletask_sql.tables.entities import events

from singletask_sql.tables import constants as names


@as_declarative()
class BaseTable(object):
    """
    Base table for ALL models (use BaseTable inherit expected for all application code)
    """
    __mapper_args__ = {
        'confirm_deleted_rows': False,
    }
    __table_args__ = {
        'extend_existing': True
    }
    id = sqla.Column(sqla.Integer, primary_key=True)
    created_at = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())

    """
    Soft delete, before query compile 
        - set is_delete = now and update record if we want deleted it
        - set filter is_delete == None if INCLUDED_DELETED == True and return only "exist" records
        
        For debugging deleted records you can use: 
        session.execute(select(Model).execution_options(constants.INCLUDED_DELETED=True))
    """
    deleted_at = sqla.Column(sqla.DateTime, nullable=True)
    updated_at = sqla.Column(sqla.DateTime, default=datetime.datetime.utcnow())

    def delete(self, deleted_at: datetime = None):
        self.deleted_at = deleted_at or datetime.datetime.utcnow()

    def restore(self):
        self.deleted_at = None


@event.listens_for(orm.Mapper, 'before_update')
def before_compile_delete(mapper, connection, entity):
    entity.updated_at = datetime.datetime.utcnow()


@event.listens_for(orm.Mapper, 'before_delete')
def before_compile_delete(mapper, connection, entity):
    raise ValueError(
        "Please use entity.delete() / entity.restore() or entity.deleted_at = datetime.datetime.utcnow()/None")


@event.listens_for(orm.Query, 'before_compile', retval=True)
def before_compile(query):
    options = query.get_execution_options()
    include_deleted = options.get(names.INCLUDED_DELETED, False)

    if include_deleted:
        return query

    for column in query.column_descriptions:
        entity = column['entity']
        if entity is None:
            continue

        query = query.enable_assertions(False).filter(
            entity.deleted_at.is_(None),
        )

    return query


class TasksTable(BaseTable, tasks.Tasks):
    __tablename__ = names.TABLE_NAME_TASKS
    performer = orm.relationship("PerformersTable")
    states = orm.relationship('TaskStatesTable', order_by="TaskStatesTable.created_at", back_populates="task")
    comments = orm.relationship('TasksCommentsTable', order_by="TasksCommentsTable.created_at", back_populates="task")
    events = orm.relationship('BaseEventsTable', order_by="BaseEventsTable.created_at", back_populates="task")


class TaskStatesTable(BaseTable, tasks.TaskStates):
    __tablename__ = names.TABLE_NAME_TASK_STATES
    task_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_TASKS}.id"))
    task = orm.relationship('TasksTable', back_populates="states")


class TasksCommentsTable(BaseTable, tasks.TaskComments):
    __tablename__ = names.TABLE_NAME_TASK_COMMENTS
    task_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_TASKS}.id"))
    task = orm.relationship('TasksTable', back_populates="comments")


class PerformersTable(BaseTable, performers.Performers):
    __tablename__ = names.TABLE_NAME_PERFORMERS
    task_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_TASKS}.id"), nullable=True)
    task = orm.relationship('TasksTable', back_populates="performer")


class BaseEventsTable(BaseTable, events.Events):
    __tablename__ = names.TABLE_NAME_EVENTS
    task_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_TASKS}.id"), nullable=True)
    task = orm.relationship('TasksTable')


class HttpEvents(BaseTable, events.HttpEvents):
    __tablename__ = names.TABLE_NAME_HTTP_EVENTS
    event_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_EVENTS}.id"), nullable=True)
    event = orm.relationship('BaseEventsTable')


class ManagersEvents(BaseTable, events.ManagerEvents):
    __tablename__ = names.TABLE_NAME_MANAGER_EVENTS
    event_id = sqla.Column(sqla.ForeignKey(f"{names.TABLE_NAME_EVENTS}.id"), nullable=True)
    event = orm.relationship('BaseEventsTable')
