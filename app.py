from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from flask_restx import Api 
from routes.data_routes import ns as ns_data
from routes.reader_routes import ns as ns_reader
from routes.sample_routes import ns as ns_sample

app = Flask(__name__)
api = Api(app=app, doc="/_docs",version='1.0.0', title='API',description='this is a api from ')

api.add_namespace(ns_data)
api.add_namespace(ns_reader)
api.add_namespace(ns_sample)

@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify(error=str(e)), e.code


if __name__ == '__main__':
    app.run(debug=True)