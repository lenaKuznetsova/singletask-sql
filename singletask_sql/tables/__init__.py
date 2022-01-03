# from sqlalchemy import orm
# import sqlalchemy as sqla
#
# from singletask_sql.tables.base import BaseTable
# from singletask_sql.tables.base.tasks import TasksTableBase, TasksStateTableBase, TaskCommentsTableBase
# from singletask_sql.tables.base.performers import PerformerTableBase
# from singletask_sql.tables.utils import Enum
#
#
# class TasksTable(TasksTableBase, BaseTable):
#     __tablename__ = 'tasks'
#     states = orm.relationship('task_states')
#     comments = orm.relationship('task_comments')
#     tasks = orm.relationship('')
#
#
# class TaskCommentsTable(BaseTable):
#     __tablename__ = 'task_comments'
#     creator_id = sqla.Column(sqla.ForeignKey("performers.id"), nullable=False)
#     task_id = sqla.Column(sqla.ForeignKey("tasks.id"), nullable=False)
#
#     text = sqla.Column(sqla.Text, nullable=False)
#
#     creator = orm.relationship('PerformersTable', back_populates='creator_comments')
#     task = orm.relationship('TasksTable', back_populates='task_comments')
#
#
# class TasksStateTable(BaseTable):
#     __tablename__ = 'task_states'
#
#     task_id = sqla.Column(sqla.ForeignKey("tasks.id"))
#     performer_id = sqla.Column(sqla.ForeignKey("performers.id"), nullable=True)
#
#     state = sqla.Column(sqla.Integer, nullable=False)
#     assign_type = sqla.Column(sqla.Integer, nullable=False)
#
#     task = orm.relationship('TasksTable')
#     performer = orm.relationship('PerformersTable')
#
#     @orm.validates('state')
#     def validate_state(self):
#         try:
#             State.to_string(self.state)
#         except IndexError:
#             raise ValueError('Invalid state')
#
#     @orm.validates('assign_type')
#     def validate_assign(self):
#         try:
#             State.to_string(self.state)
#         except IndexError:
#             raise ValueError('Invalid assign type')
