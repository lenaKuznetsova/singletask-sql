from unittest import TestCase

from singletask_sql.settings import BASE_DIR, dotenv_values
from singletask_sql.engine import create_engine

env_path = [
    f'{BASE_DIR}/../.env',
    f'{BASE_DIR}/../.env.local',
    f'{BASE_DIR}/../.env.tests',
]
conf = {}
for path in env_path:
    conf.update(dotenv_values(path))


class DBTestCase(TestCase):
    sql_engine = create_engine(conf)
