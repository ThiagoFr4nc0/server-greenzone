from controller.abstract_controller import AbstractRepository
from model.DTO.sample_dto import SampleDTO
from model.DTO.data_dto import DataDTO

class SampleRepository(AbstractRepository):

    def __init__(self):
        super().__init__(SampleDTO)

    def delete_all(self, sample_id):
        sample_current:SampleDTO = self.find(sample_id)
        label_current:DataDTO = self.find(sample_current.label)
        label_current.sample_id = None
        self._session.query(DataDTO).filter(DataDTO.id == sample_current.label).delete()
        sample_current.label = None
        self._session.delete(sample_current)
        self._session.commit()
