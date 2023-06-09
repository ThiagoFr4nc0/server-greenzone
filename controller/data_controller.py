from controller.abstract_controller import AbstractRepository
from model.DTO.data_dto import DataDTO

class DataRepository(AbstractRepository):

    def __init__(self):
        super().__init__(DataDTO)

    def update(self, id, data:DataDTO):
        data_current = self.find(id)

        self._session.commit()
