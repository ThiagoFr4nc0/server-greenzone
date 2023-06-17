from sqlalchemy import Column, Integer, Sequence, String, Date
from connection.base import Base

class ReaderDTO(Base):
    __tablename__ = 'reader'

    id = Column(Integer, Sequence('seq_reader_pk'), primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    lot = Column(Integer, nullable = False)
    manufac_date = Column(Date, nullable=False) 
    buy_date = Column(Date, nullable=False)
    type = Column(String, nullable=False)

    #   || ID ||  Code  || Manufac_Date ||   Buy_Date  ||     Type     ||
    #   || 1  || SS001  ||  19/05/2023  ||  01/06/2023 ||   NPK SOIL   ||
    #   || 2  || SSP001 ||  19/05/2023  ||  02/06/2023 ||  NPKTH SOIL  ||
    #   || 3  || SS002  ||  20/05/2023  ||  02/06/2023 ||   NPK SOIL   ||