from controller.abstract_controller import AbstractRepository
from model.DTO.data_dto import DataDTO

class DataRepository(AbstractRepository):

    def __init__(self):
        super().__init__(DataDTO)

    def update(self, id, data:DataDTO):
        data_current = self.find(id)
        
        data_current.label = data.label
        data_current.nitrogen = data.nitrogen
        data_current.phosphor = data.phosphor
        data_current.potassium = data.potassium
        data_current.humidity = data.humidity
        data_current.temperature = data.temperature

        self._session.commit()

    def patch_close (self, id, sample_id:int):
        data_current = self.find(id)
        data_current.sample_id = sample_id

        self._session.commit()
