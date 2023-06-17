from model.VO.reader_vo import ReaderVO
from model.DTO.reader_dto import ReaderDTO
from controller.reader_controller import ReaderRepository
from datetime import date

class ReaderService():

    __reader_repository = ReaderRepository()

    def save_reader(self, data:ReaderVO):
        self.__reader_repository.add(data.toDto())
    
    def get_all_reader(self):
        vos = []
        dtos = self.__reader_repository.find_all()

        for dto in dtos:
            vos.append(ReaderVO.fromDto(dto))
        return vos
    
    def find_reader(self, id):
        dto:ReaderDTO = self.__reader_repository.find(id)
        if dto is None:
            raise IndexError("Movie not found")
        
        return ReaderVO.fromDto(dto)
    
    def update_data(self, id , reader:ReaderVO):
        self.__reader_repository.update(id, reader.toDto())

    def patch_buy_date(self, id, date:date):
        self.__reader_repository.patch_buy_date(id,date)
    
    def delete_data(self, id):
        data = self.__reader_repository.find(id)
        if data is None:
            raise IndexError("Movie not found") 
        
        self.__reader_repository.delete(data)
    