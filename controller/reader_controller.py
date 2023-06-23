from controller.abstract_controller import AbstractRepository
from model.DTO.reader_dto import ReaderDTO
from model.DTO.sample_dto import SampleDTO
from datetime import date

class ReaderRepository(AbstractRepository):

    def __init__(self):
        super().__init__(ReaderDTO)

    def update(self, id, reader:ReaderDTO):
        reader_current = self.find(id)
        
        reader_current.model = reader.model
        reader_current.lot = reader.lot
        reader_current.manufac_date = reader.manufac_date
        reader_current.buy_date = reader.buy_date
        reader_current.type = reader.type

        self._session.commit()
    
    def patch_buy_date(self, id, date:date):
        reader_current:ReaderDTO = self.find(id)

        reader_current.buy_date = date

        self._session.commit()

    def delete_all_by_reader(self, id):
        reader_current:ReaderDTO = self.find(id)
        self._session.query(SampleDTO).filter(SampleDTO.code == reader_current.id).delete()
        self._session.delete(reader_current)
        self._session.commit()

        
