from flask import Blueprint

Login_blueprint = Blueprint('Login_blueprint', __name__)

@Login_blueprint.route('/user')
def index():
    return "This is an example app"