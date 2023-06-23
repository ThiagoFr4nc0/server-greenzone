from controller.reader_controller import ReaderDTO
from helper.validations import Validations
    
class ReaderVO():

    def __init__(self):
        self.id = None
        self.model = ''
        self.lot = None 
        self.manufac_date = 0 
        self.buy_date = 0 
        self.type = ''


    @staticmethod
    def fromDto(dto:ReaderDTO):
        vo = ReaderVO()
        vo.id = dto.id
        vo.model = dto.model
        vo.lot = dto.lot
        vo.manufac_date = str(dto.manufac_date)
        vo.buy_date = str(dto.buy_date)
        vo.type = dto.type

        return vo
    
    def fromJson(self, json): 
        self.model = Validations._is_text_empty_validation(json,'model')
        self.lot = Validations._is_elements_empty_validation(json,'lot')
        self.manufac_date = Validations._is_date_validation(json,'manufac_date')
        self.buy_date = None
        self.type = Validations._is_text_empty_validation(json,'type')
    
    def toDto(self):
        dto = ReaderDTO()
        dto.id = self.id
        dto.model = self.model
        dto.lot = self.lot
        dto.manufac_date = self.manufac_date
        dto.buy_date = self.buy_date
        dto.type = self.type

        return dto

    def toJson(self):
        json = self.__dict__.copy()
        return json