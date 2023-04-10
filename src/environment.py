import os

import environ

env = environ.Env()
current_path = environ.Path(__file__) - 1
env_file = current_path(".env")

if os.path.exists(env_file):
    environ.Env.read_env(env_file=env_file)
