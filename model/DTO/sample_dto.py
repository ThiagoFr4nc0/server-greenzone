from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey,Sequence, Date
from connection.base import Base

class SampleDTO(Base):
    __tablename__ = 'sample'

    id = Column(Integer, Sequence('seq_sample_pk'), primary_key=True, autoincrement=True)
    code = Column(Integer, ForeignKey("reader.id"), nullable=False)#relationship("ReaderDTO")
    reading_Date = Column(Date, nullable=False)
    label = Column(Integer, ForeignKey("data.id"), nullable=False)#relationship("DataDTO")

    #   || ID ||  Code  || Reading_Date ||   Class   ||
    #   || 1  ||   FK   ||  05/06/2023  ||    rice   ||    
    #   || 2  ||   FK   ||  05/06/2023  ||   coffee  || 
    #   || 3  ||   FK   ||  06/06/2023  ||    mango  ||