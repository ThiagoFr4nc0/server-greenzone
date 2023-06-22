from helper.communs import communs
from flask_restx import Resource,Namespace,fields
from model.VO.sample_vo import SampleVO
from flask import request, abort, jsonify
from service.sample_service import SampleService

ns = Namespace('sample',description='routes of sample model')

sample_model = ns.model('sample', {
    'id': fields.Integer(required=False, description = 'sample id'),
    'code' : fields.Integer(required=True, description = 'sample id'),
    'reading_Date' : fields.Date(required=True, description = 'sample id'),
    'label' : fields.Integer(required=True, description = 'sample id'),
})

@ns.route('')
class DatasRoutes(Resource):

    _sample_service = SampleService()

    @ns.response(200,"Sucess",sample_model)
    def get(self):
        return communs._toJsonFromArray(self._sample_service.get_all_sample())

    @ns.expect(sample_model)
    def post(self):
        body = request.get_json()

        try:
            sample = SampleVO()
            sample.fromJson(body)
        except ValueError as e:
            abort(400, e)
        
        self._sample_service.save_sample(sample)
        return jsonify(success='Sample save with success')

@ns.route('/<int:id>')
class DataRoutes(Resource):

    _sample_service = SampleService()

    def get(self, id):
        if id < 1:
            abort(403, "Invalid identifier")
        
        try:
            sample = self._sample_service.find_sample(id)
        except IndexError as e:
            abort(404, str(e))

        return sample.toJsonSimple()
    
    
    def delete(self,id):
        if id < 1:
            abort(403,'Invalid identifier')
        try:
            self._sample_service.delete_sample(id)
        except IndexError as e:
            abort(404, str(e))
        return jsonify(sucecess='Sample deleted eith success')

