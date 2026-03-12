import environ

env = environ.Env()
environ.Env.read_env()

ENV = env("ENV")

if ENV == "local":
    from .local import *
if ENV == "prod":
    from .prod import *
if ENV == "test":
    from .test import *
