import environ

env = environ.Env()
environ.Env.read_env()

env = env("ENV")

if env == "local":
    from .local import *
if env == "prod":
    from .prod import *
if env == "test":
    from .test import *
