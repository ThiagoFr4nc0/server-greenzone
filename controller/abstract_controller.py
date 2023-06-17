from typing import Generic, TypeVar
from connection.db_cofig import DBConfig
from sqlalchemy.orm import sessionmaker,lazyload

M = TypeVar('M')

class AbstractRepository(Generic[M]):
    __class = None #PRIVATE
    _session = None #PROTECTED

    def __init__(self, klass):
        __db = DBConfig.create()
        session = sessionmaker(bind=__db.engine)  
        self._session = session()
        self.__class = klass

    def add(self, model:M):
        self._session.add(model)
        self._session.commit()

    def delete(self, model:M):
        self._session.delete(model)
        self._session.commit()

    def find_all(self):
        return self._session.query(self.__class)
    
    def find(self, id):
        #self._session.query(self.__class).options(lazyload(atribute)).get(id)
        return self._session.query(self.__class).get(id)