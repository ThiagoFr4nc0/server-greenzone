from helper.communs import communs
from flask_restx import Resource,Namespace,fields
from model.VO.data_vo import DataVO
from flask import request, abort, jsonify, send_file
from service.data_service import DataService

ns = Namespace('data',description='routes of data model')

data_model = ns.model('data', {
    'id': fields.Integer(required=True, description = 'data id'),
    'label' : fields.String(required=True, description = 'data id'),
    'nitrogen' : fields.Float(required=True, description = 'data id'),
    'phosphor' : fields.Float(required=True, description = 'data id'),
    'potassium' : fields.Float(required=True, description = 'data id'),
    'temperature' : fields.Integer(required=True, description = 'data id'),
    'humidity' : fields.Integer(required=True, description = 'data id'),

})

@ns.route('')
class DataRoutes(Resource):

    _data_service = DataService()

    @ns.response(200,"Sucess",data_model)
    def get(self):
        return communs._toJsonFromData(self._data_service.get_all_data())

    @ns.expect(data_model)
    def post(self):
        body = request.get_json()

        try:
            data = DataVO()
            data.fromJson(body)
        except ValueError as e:
            abort(400, e)
        
        self._data_service.save_data(data)
        return jsonify(success='Data save with success')