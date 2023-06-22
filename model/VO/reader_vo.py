from datetime import date , datetime
from controller.reader_controller import ReaderDTO

    
class ReaderVO():

    def __init__(self):
        self.id = None
        self.model = ''
        self.lot = None 
        self.manufac_date = 0 
        self.buy_date = 0 
        self.type = ''

    
    def _is_text_empty_validation(self, json, att_name):
        if not att_name in json or json[att_name] is None or not json[att_name].strip():
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]

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
        self.model = self._is_text_empty_validation(json,'model')
        self.lot = self._is_elements_empty_validation(json,'lot')
        self.manufac_date = self._is_date_validation(json,'manufac_date')
        self.buy_date = None
        self.type = self._is_text_empty_validation(json,'type')
    
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