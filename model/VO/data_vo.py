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
        self.label = json['label']
        self.nitrogen = json['nitrogen']
        self.phosphor = json['phosphor']
        self.potassium = json['potassium']
        self.temperature = json['temperature']
        self.humidity = json['humidity']
    
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