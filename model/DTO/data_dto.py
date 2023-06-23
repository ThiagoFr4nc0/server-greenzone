from sqlalchemy import Column, Integer,ForeignKey, Sequence, String, Double 
from connection.base import Base
from sqlalchemy.orm import relationship
class DataDTO(Base):
    __tablename__ = 'data'

    id = Column(Integer, Sequence('seq_data_pk'), primary_key=True, autoincrement=True)
    label = Column(String, nullable=False)
    nitrogen = Column(Double, nullable=False) 
    phosphor = Column(Double, nullable=False)
    potassium = Column(Double, nullable=False)
    temperature = Column(Integer, nullable=True)
    humidity = Column(Integer, nullable=True)
    sample_id = Column(Integer, ForeignKey("sample.id"), nullable=True)
    #   || ID ||   label  ||  Nitrogen   ||   Phosphor   ||   Potassium   ||  Temperature  ||  humidity  ||
    #   || 1  ||   rice   ||    11.0     ||      7.5     ||     12.9      ||      20       ||     80     ||    
    #   || 2  ||  coffee  ||    18.5     ||      9.4     ||     10.1      ||      18       ||     38     || 
    #   || 3  ||   mango  ||    13.6     ||     10.0     ||      5.9      ||      22       ||     42     ||