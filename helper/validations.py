from datetime import date , datetime

class Validations() :
    def _is_text_empty_validation(json, att_name):
        if not att_name in json or json[att_name] is None or not json[att_name].strip():
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]

    def _is_elements_empty_validation(json, att_name):
        if not att_name in json or json[att_name] is None or not isinstance(json[att_name], int) or json[att_name] <= 0:
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]
    
    def _is_date_validation( json, att_name):
        datetime_obj:datetime = datetime.strptime(json[att_name], '%Y-%m-%d')  
        if not att_name in json or json[att_name] is None or  datetime_obj.date() > date.today():
            raise ValueError(f"The attribute {att_name} is invalid!")
        return json[att_name]