from datetime import datetime
from controller.data_controller import DataDTO

class DataVO():

    def __init__(self):
        self.id = None
        self.label = ''
        self.nitrogen = 0 
        self.phosphor = 0
        self.potassium = 0
        self.temperature = 0
        self.humidity = 0

    
    def _is_text_empty_validation(self, json, att_name):
        if not att_name in json or json[att_name] is None or not json[att_name].strip():
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]

    def _is_elements_empty_validation(self, json, att_name):
        if not att_name in json or json[att_name] is None or not isinstance(json[att_name], int) or json[att_name] <= 0:
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]
    
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

        return vo
    
    def fromJson(self, json): 
        self.label =  self._is_text_empty_validation(json,'label')
        self.nitrogen = self._is_elements_empty_validation(json,'nitrogen')
        self.phosphor = self._is_elements_empty_validation(json,'phosphor')
        self.potassium = self._is_elements_empty_validation(json,'potassium')
        self.temperature = self._is_elements_empty_validation(json,'temperature')
        self.humidity = self._is_elements_empty_validation(json,'humidity')
    
    def toDto(self):
        dto = DataDTO()
        dto.id = self.id
        dto.label = self.label
        dto.nitrogen = self.nitrogen
        dto.phosphor = self.phosphor
        dto.potassium = self.potassium
        dto.temperature = self.temperature
        dto.humidity = self.humidity

        return dto

    def toJson(self):
        json = self.__dict__.copy()
        return json