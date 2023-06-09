from model.VO.data_vo import DataVO
from model.DTO.data_dto import DataDTO
from controller.data_controller import DataRepository
import os

class DataService():

    __data_repository = DataRepository()

    def save_data(self, data:DataVO):
        self.__data_repository.add(data.toDto())
    
    def get_all_data(self):
        vos = []
        dtos = self.__data_repository.find_all()
        
        for dto in dtos:
            vos.append(DataVO.fromDto(dto))
        
        return vos
    
    def find_data(self, id):
        dto:DataDTO = self.__data_repository.find(id)
        if dto is None:
            raise IndexError("Movie not found")
        
        return DataVO.fromDto(dto)
    
    def delete_data(self, id):
        data = self.__data_repository.find(id)
        if data is None:
            raise IndexError("Movie not found") 
        
        self.__data_repository.delete(data)
    