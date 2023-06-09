from connection.base import Base
from sqlalchemy import create_engine

from model.DTO.data_dto import DataDTO

class DBConfig:    
    
    __instance = None #Private

    def __init__(self):
        if DBConfig.__instance is not None:
            raise Exception("This class is a singleton, use DB.create_engine")
        else:
            DBConfig.__instance = self
        self.engine = self.create_connection()
    
    def create_connection(self):

        #Connection String DB
        #db_string = "postgresql://postgres:root@localhost:5432/postgres"
        db_string = "postgresql://postgres:root@127.0.0.1:5432/api"
        conn = create_engine(db_string)
        
        Base.metadata.create_all(conn.engine)
        print(conn.connect)
        return conn
    
    @staticmethod
    def create():
        if DBConfig.__instance is None:
            DBConfig.__instance = DBConfig()
        
        return DBConfig.__instance