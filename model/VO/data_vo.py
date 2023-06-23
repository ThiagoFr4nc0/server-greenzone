from controller.data_controller import DataDTO
from helper.validations import Validations
class DataVO():

    def __init__(self):
        self.id = None
        self.label = ''
        self.nitrogen = 0 
        self.phosphor = 0
        self.potassium = 0
        self.temperature = 0
        self.humidity = 0
        self.sample_id = 0

    
    
    @staticmethod
    def fromDto(dto:DataDTO):
        vo = DataVO()
        vo.id = dto.id
        vo.label = dto.label
        vo.nitrogen = dto.nitrogen
        vo.phosphor = dto.phosphor
        vo.potassium = dto.potassium
        vo.temperature = dto.temperature
        vo.humidity = dto.humidity
        vo.sample_id = dto.sample_id

        return vo
    
    def fromJson(self, json): 
        self.label =  Validations._is_text_empty_validation(json,'label')
        self.nitrogen = Validations._is_elements_empty_validation(json,'nitrogen')
        self.phosphor = Validations._is_elements_empty_validation(json,'phosphor')
        self.potassium = Validations._is_elements_empty_validation(json,'potassium')
        self.temperature = Validations._is_elements_empty_validation(json,'temperature')
        self.humidity = Validations._is_elements_empty_validation(json,'humidity')
        self.sample_id = None
    
    def toDto(self):
        dto = DataDTO()
        dto.id = self.id
        dto.label = self.label
        dto.nitrogen = self.nitrogen
        dto.phosphor = self.phosphor
        dto.potassium = self.potassium
        dto.temperature = self.temperature
        dto.humidity = self.humidity
        dto.sample_id = self.sample_id

        return dto

    def toJson(self):
        json = self.__dict__.copy()
        return json