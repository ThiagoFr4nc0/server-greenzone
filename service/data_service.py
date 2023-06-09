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
    