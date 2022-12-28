import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

class Database:
    __conn = None

    @staticmethod
    def conn():
        if Database.__conn == None:
            engine = create_engine(
                f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}",
                isolation_level="READ UNCOMMITTED"
            )
            Session = sessionmaker(bind=engine)
            Database.__conn = Session()

        return Database.__conn

db = Database.conn()

