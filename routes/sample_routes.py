from helper.communs import communs
from flask_restx import Resource,Namespace,fields
from model.VO.sample_vo import SampleVO
from flask import request, abort, jsonify ,send_file
from service.data_service import DataService
from service.reader_servico import ReaderService
from service.sample_service import SampleService

ns = Namespace('sample',description='routes of sample model')

sample_model = ns.model('sample', {
    'id': fields.Integer(required=False, description = 'sample id'),
    'code' : fields.Integer(required=True, description = 'sample id'),
    'reading_Date' : fields.Date(required=True, description = 'sample id'),
    'label' : fields.Integer(required=True, description = 'sample id'),
})

@ns.route('')
class SamplesRoutes(Resource):

    _sample_service = SampleService()

    @ns.response(200,"Sucess",sample_model)
    def get(self):
        return communs._toJsonFromSimple(self._sample_service.get_all_sample())

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
class SampleRoutes(Resource):

    _sample_service = SampleService()
    _data_service = DataService()
    _reader_service = ReaderService()

    def get(self, id):
        if id < 1:
            abort(403, "Invalid identifier")
        
        try:
            sample = self._sample_service.find_sample(id)
            code = self._reader_service.find_reader(sample.code)
            label = self._data_service.find_data(sample.label)
        except IndexError as e:
            abort(404, str(e))

        return sample.toJsonFull(code , label)
    

    
    def patch(self,id):
        if id < 1:
            abort(403, "Invalid identifier")
        try:
            sample = self._sample_service.find_sample(id)
        except ValueError as e:
            abort(400, e)
        self._sample_service.patch_close(sample)
        return jsonify(success='Data save with success')
    
    def delete(self,id):
        if id < 1:
            abort(403,'Invalid identifier')
        try:
            self._sample_service.delete_sample(id)
        except IndexError as e:
            abort(404, str(e))
        return jsonify(sucecess='Sample deleted eith success')
    

@ns.route('/<int:id>/review')
class SampleReviewEndpoint(Resource):
    _sample_service = SampleService()

    #@ns.doc(params={'id':'id of Movie'}, description='Get a review of movie by ID')
    @ns.response(200, 'Success')
    @ns.response(403, 'Invalid identifier')
    @ns.response(404, 'Movie not found')
    def get(self, id):
        if id < 1:
            abort(403, "Invalid idenfier")
        try:
            self._sample_service.find_sample(id)
            filename = self._sample_service.find_file(str(id))
            return send_file(filename, mimetype='image/jpeg')
        except IndexError or FileNotFoundError as e:
            abort(404, str(e))

    #@ns.doc(params={'id':'id of Movie'}, description='Save a review of movie by ID')
    @ns.response(200, 'Success')
    @ns.response(400, 'Invalid values attributes')
    @ns.response(403, 'Invalid identifier')
    @ns.response(404, 'Movie not found')
    @ns.response(409, 'Movie has a review')
    @ns.response(413, 'Invalid file size')
    def post(self, id):
        if id < 1:
            abort(403, "Invalid idenfier")
        
        if 'file' not in request.files:
            abort(400, "The review is required")

        file = request.files['file']
        if file.filename.strip() == '' or not communs._allowed_file(file.filename):
            abort(400, f'invalid file, extension files are allowed {communs.ALLOWED_EXTENSIONS}')
        
        blob = file.read()
        if len(blob) == 0 or len(blob) / (1024 * 1024) > 16:
            abort(413, 'invalid file size (Max. 16mb)')

        try:
            sample = self._sample_service.find_sample(id)
            current_file = self._sample_service.find_file(str(id))
            if current_file:
                abort(409, f'Movie {sample.id} has a review.')
        except IndexError as e:
            abort(404, str(e))
        except FileNotFoundError:
            pass

        self._sample_service.save_file(file,blob,id)
        return jsonify(success="Movie review has been successfully added!")

