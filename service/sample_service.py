from model.VO.sample_vo import SampleVO
from model.DTO.sample_dto import SampleDTO
from controller.sample_controller import SampleRepository
from controller.data_controller import DataRepository
from controller.reader_controller import ReaderRepository

class SampleService():

    __sample_repository = SampleRepository()
    __data_repository = DataRepository()
    __reader_repository = ReaderRepository()

    def save_sample(self, sample:SampleVO):
        sample_dto:SampleDTO = sample.toDto()

        self.__data_repository.patch_close(sample_dto.label , sample_dto.id)
        self.__reader_repository.patch_close(sample_dto.code , sample_dto.id)
        self.__sample_repository.add(sample_dto)
    
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
    