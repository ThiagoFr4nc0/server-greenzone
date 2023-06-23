from model.VO.sample_vo import SampleVO
from model.DTO.sample_dto import SampleDTO
from controller.sample_controller import SampleRepository
from controller.data_controller import DataRepository
from controller.reader_controller import ReaderRepository
import os

class SampleService():

    STORAGE_PATH = '/home/thiagofranco/IF/API/server-greenzone/imgs'

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


    def find_file(self, name):
        for path, _, files in os.walk(self.STORAGE_PATH): 
            for filename in files:
                if name in filename:
                    return os.path.join(path, filename)
        raise FileNotFoundError('File not found')
    
    def save_file(self, file , id):
        blob = file.read()
        filename = str(id) + '.' + file.filename.split('.')[-1]
        file_image = open(os.path.join(self.STORAGE_PATH, filename), 'wb')
        file_image.write(blob)
        file_image.close()
    