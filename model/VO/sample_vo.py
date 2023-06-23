from controller.sample_controller import SampleDTO
from helper.validations import Validations

class SampleVO():

    def __init__(self):
        self.id = None
        self.code = 0
        self.reading_Date = 0
        self.label = 0

    @staticmethod
    def fromDto(dto:SampleDTO):
        vo = SampleVO()
        vo.id = dto.id
        vo.code = dto.code
        vo.reading_Date = str(dto.reading_Date)
        vo.label = dto.label

        return vo
    
    def fromJson(self, json): 
        self.code = Validations._is_elements_empty_validation(json,'code')
        self.reading_Date = Validations._is_date_validation(json,'reading_Date')
        self.label = Validations._is_elements_empty_validation(json,'label')
    
    def toDto(self):
        dto = SampleDTO()
        dto.id = self.id
        dto.code = self.code
        dto.reading_Date = self.reading_Date
        dto.label = self.label

        return dto

    def toJsonSimple(self):
        json = {}
        json['id'] = self.id
        json['code'] = self.code
        json['reading_Date'] = str(self.reading_Date)
        json['label'] = self.label
        return json

    def toJsonFull(self, code, label):
        json = {}
        json['id'] = self.id
        json['code'] = code.__dict__.copy()
        json['reading_Date'] = str(self.reading_Date)
        json['label'] = label.__dict__.copy()
        return json

