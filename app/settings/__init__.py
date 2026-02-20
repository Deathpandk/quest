import environ

env = environ.Env()
environ.Env.read_env()

env = env("ENV")

if env == "local":
    pass
if env == "prod":
    pass
if env == "test":
    pass
