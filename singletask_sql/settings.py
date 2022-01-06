import os
from dotenv import dotenv_values

BASE_DIR = os.path.dirname(__file__)
env_path = [
    f'{BASE_DIR}/../.env',
    f'{BASE_DIR}/../.env.local'
]
conf = {}
for path in env_path:
    conf.update(dotenv_values(path))

