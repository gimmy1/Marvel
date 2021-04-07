import os

class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DATABASE = {
        "user": os.getenv("DATABASE_USERNAME"),
        "password": os.getenv("DATABASE_PASSWORD"),
        "host": os.getenv("DATABASE_HOST"),
        "port": os.getenv("DATABASE_PORT"),
        "dbname": os.getenv("DATABASE_NAME")
    }

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    pass