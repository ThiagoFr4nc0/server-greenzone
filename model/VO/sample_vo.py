from controller.sample_controller import SampleDTO
from datetime import date , datetime

class SampleVO():

    def __init__(self):
        self.id = None
        self.code = 0
        self.reading_Date = 0
        self.label = 0

    def _is_elements_empty_validation(self, json, att_name):
        if not att_name in json or json[att_name] is None or not isinstance(json[att_name], int) or json[att_name] <= 0:
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]
    
    def _is_date_validation(self, json, att_name):
        datetime_obj:datetime = datetime.strptime(json[att_name], '%Y-%m-%d')  
        if not att_name in json or json[att_name] is None or  datetime_obj.date() > date.today():
           raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]

    @staticmethod
    def fromDto(dto:SampleDTO):
        vo = SampleVO()
        vo.id = dto.id
        vo.code = dto.code
        vo.reading_Date = str(dto.reading_Date)
        vo.label = dto.label

        return vo
    
    def fromJson(self, json): 
        self.code = self._is_elements_empty_validation(json,'code')
        self.reading_Date = self._is_date_validation(json,'reading_Date')
        self.label = self._is_elements_empty_validation(json,'label')
    
    def toDto(self):
        dto = SampleDTO()
        dto.id = self.id
        dto.code = self.code
        dto.reading_Date = self.reading_Date
        dto.label = self.label

        return dto

    def toJsonSimple(self):
        json = []
        json['id'] = self.id.__dict__.copy()
        json['code'] = self.code.__dict__.copy()
        json['reading_Date'] = self.reading_Date.__dict__.copy()
        json['label'] = self.label.__dict__.copy()
        return json

    def toJsonFull(self, code, label):
        json = []
        json['id'] = self.id.__dict__.copy()
        json['code'] = code.__dict__.copy()
        json['reading_Date'] = self.reading_Date.__dict__.copy()
        json['label'] = label.__dict__.copy()
        return json

