from model.VO.sample_vo import SampleVO
from model.DTO.sample_dto import SampleDTO
from controller.sample_controller import SampleRepository

class SampleService():

    __sample_repository = SampleRepository()

    def save_sample(self, sample:SampleVO):
        self.__sample_repository.add(sample.toDto())
    
    def get_all_sample(self):
        vos = []
        dtos = self.__sample_repository.find_all()
        
        for dto in dtos:
            vos.append(SampleVO.fromDto(dto))
        
        return vos
    
    def find_sample(self, id):
        dto:SampleDTO = self.__sample_repository.find(id)
        if dto is None:
            raise IndexError("Movie not found")
        
        return SampleVO.fromDto(dto)
    
    
    def delete_sample(self, id):
        sample = self.__sample_repository.find(id)
        if sample is None:
            raise IndexError("Movie not found") 
        
        self.__sample_repository.delete(sample)
    