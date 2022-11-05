import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@database/flask"
    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

