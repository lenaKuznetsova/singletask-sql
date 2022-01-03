import os
from dotenv import dotenv_values

BASE_DIR = os.path.dirname(__file__)
env_path = [
    f'{BASE_DIR}/../.env',
    f'{BASE_DIR}/../.env.local',
    f'{BASE_DIR}/../.env.tests',
]
conf = {}
for path in env_path:
    conf.update(dotenv_values(path))

