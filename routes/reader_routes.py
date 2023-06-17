from helper.communs import communs
from flask_restx import Resource,Namespace,fields
from model.VO.reader_vo import ReaderVO
from flask import request, abort, jsonify
from service.reader_servico import ReaderService
from datetime import date

ns = Namespace('reader',description='routes of reader model')

reader_model = ns.model('reader', {
    'id': fields.Integer(required=False, description = 'data id'),
    'model' : fields.String(required=True, description = 'model id'),
    'lot' : fields.Integer(required=True, description = 'data id'),
    'manufac_date' : fields.Date(required=True, description = 'data id'),
    'buy_date' : fields.Date(required=True, description = 'data id'),
    'type' : fields.String(required=True, description = 'data id'),

})

reader_buy_date = ns.model('buy date', {
    'date': fields.Date(required=False, description = 'data id'),
})

@ns.route('')
class ReaderRoutes(Resource):

    _reader_service = ReaderService()

    @ns.response(200,"Sucess",reader_model)
    def get(self):
        return communs._toJsonFromArray(self._reader_service.get_all_reader())

    @ns.expect(reader_model)
    def post(self):
        body = request.get_json()

        try:
            data = ReaderVO()
            data.fromJson(body)
        except ValueError as e:
            abort(400, e)
        
        self._reader_service.save_reader(data)
        return jsonify(success='Data save with success')

@ns.route('/<int:id>')
class DataRoutes(Resource):

    _reader_service = ReaderService()

    def get(self, id):
        if id < 1:
            abort(403, "Invalid identifier")
        
        try:
            data = self._reader_service.find_reader(id)
        except IndexError as e:
            abort(404, str(e))

        return data.toJson()
    
    @ns.expect(reader_model)
    def put(self,id):
        body = request.get_json()
        try:
            data = ReaderVO()
            data.fromJson(body)
        except ValueError as e:
            abort(400, e)
        self._reader_service.update_data(id,data)
        return jsonify(success='Data save with success')
    
    @ns.expect(reader_buy_date)
    def patch(self,id):
        body = request.get_json()
        try:
            date_currente:date = body['date']
        except ValueError as e:
            abort(400, e)
        self._reader_service.patch_buy_date(id,date_currente)
        return jsonify(success='Data save with success')
    
    def delete(self,id):
        if id < 1:
            abort(403,'Invalid identifier')
        try:
            self._reader_service.delete_data(id)
        except IndexError as e:
            abort(404, str(e))
        return jsonify(sucecess='Data deleted eith success')
