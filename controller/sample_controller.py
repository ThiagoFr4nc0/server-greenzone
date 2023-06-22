from controller.abstract_controller import AbstractRepository
from model.DTO.sample_dto import SampleDTO

class SampleRepository(AbstractRepository):

    def __init__(self):
        super().__init__(SampleDTO)
